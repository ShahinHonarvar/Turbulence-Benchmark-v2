from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_count[tuple(sorted(word.lower()))] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 34