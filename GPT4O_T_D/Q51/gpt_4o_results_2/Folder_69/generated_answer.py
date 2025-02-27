from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_chars = ''.join(sorted(string.lower()))
            anagram_counts[sorted_chars] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 58