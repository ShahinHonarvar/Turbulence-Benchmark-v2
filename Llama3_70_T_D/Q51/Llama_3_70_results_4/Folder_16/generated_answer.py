def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        sorted_string = ''.join(sorted(s))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(s)
        else:
            anagrams[sorted_string] = [s]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 24