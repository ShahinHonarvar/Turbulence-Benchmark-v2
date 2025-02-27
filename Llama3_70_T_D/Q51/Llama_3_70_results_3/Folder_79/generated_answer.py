from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(set)
    for string in lst:
        lower_string = ''.join(filter(str.isalpha, string)).lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagrams[sorted_string].add(lower_string)
    pairs = sum((len(strings) * (len(strings) - 1) // 2 for strings in anagrams.values()))
    return pairs <= 173