from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            anagram_count[tuple(sorted(word))] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return total_pairs <= 416