from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            anagrams[''.join(sorted(string.lower()))].append(string)
    total_anagrams = sum((max(0, len(value) - 1) for value in anagrams.values()))
    return total_anagrams >= 233