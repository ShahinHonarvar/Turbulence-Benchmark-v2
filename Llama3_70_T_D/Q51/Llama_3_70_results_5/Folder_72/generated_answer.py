def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(filter(str.isalpha, string.casefold())))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 188