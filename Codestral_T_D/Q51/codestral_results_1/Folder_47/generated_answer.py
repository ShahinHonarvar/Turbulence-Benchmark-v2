from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_count[tuple(sorted(word.lower()))] += 1
    return sum((val * (val - 1) // 2 for val in anagram_count.values())) <= 366