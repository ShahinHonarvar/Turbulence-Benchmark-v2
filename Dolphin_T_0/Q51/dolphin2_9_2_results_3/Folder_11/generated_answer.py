from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        lower_str = string.lower()
        if len(lower_str) < 3:
            continue
        sorted_str = ''.join(sorted(lower_str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(lower_str)
    pairs = 0
    for values in anagrams.values():
        if len(values) > 1:
            pairs += len(values) * (len(values) - 1) // 2
        if pairs > 41:
            return False
    return True