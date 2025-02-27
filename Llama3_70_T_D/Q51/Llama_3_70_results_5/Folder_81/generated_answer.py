def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        temp = ''.join(filter(str.isalpha, string)).lower()
        if len(temp) < 3:
            continue
        sorted_str = ''.join(sorted(temp))
        if sorted_str in anagrams:
            count += anagrams[sorted_str]
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return count <= 79