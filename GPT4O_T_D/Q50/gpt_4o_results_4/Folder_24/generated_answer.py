from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_counts[sorted_string] += 1
    total_anagram_pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            total_anagram_pairs += count * (count - 1) // 2
    return total_anagram_pairs >= 65