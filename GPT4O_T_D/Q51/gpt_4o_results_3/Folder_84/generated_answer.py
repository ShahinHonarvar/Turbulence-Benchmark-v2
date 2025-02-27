from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_tuple = tuple(sorted(string.lower()))
            anagram_counts[sorted_tuple] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_of_anagrams <= 16