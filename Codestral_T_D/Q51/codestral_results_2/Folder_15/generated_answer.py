from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_counts[tuple(sorted(word.lower()))] += 1
    return sum((n * (n - 1) // 2 for n in anagram_counts.values())) <= 20