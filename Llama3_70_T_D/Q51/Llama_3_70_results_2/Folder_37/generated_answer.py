def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            count += len(anagrams[sorted_str])
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]
    return count <= 206