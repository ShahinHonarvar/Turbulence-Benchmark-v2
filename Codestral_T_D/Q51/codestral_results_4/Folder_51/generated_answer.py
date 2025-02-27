from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            anagram_counts[sorted_s] = anagram_counts.get(sorted_s, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 116