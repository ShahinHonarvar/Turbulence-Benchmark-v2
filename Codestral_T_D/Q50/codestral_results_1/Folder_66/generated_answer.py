from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_counts[sorted_s] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 92