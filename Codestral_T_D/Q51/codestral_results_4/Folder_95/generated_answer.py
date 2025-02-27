from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((val * (val - 1) // 2 for val in anagrams.values())) <= 6