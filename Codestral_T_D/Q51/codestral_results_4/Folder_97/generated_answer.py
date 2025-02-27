from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_counts[sorted_string] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pair_count <= 18