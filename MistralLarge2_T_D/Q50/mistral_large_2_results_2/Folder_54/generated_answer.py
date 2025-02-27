from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_count[sorted_string].append(string)
    pairs_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_count.values()))
    return pairs_count >= 74