from collections import Counter

def if_contains_anagrams(strings):

    def count_anagram_pairs(counter, n):
        return n * (n - 1) // 2
    anagram_counts = Counter()
    for s in strings:
        if len(s) >= 3:
            anagram_counts[frozenset(Counter(s.lower()))] += 1
    return sum((count_anagram_pairs(count, n) for n in anagram_counts.values())) <= 423