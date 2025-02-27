from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_counts[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 49