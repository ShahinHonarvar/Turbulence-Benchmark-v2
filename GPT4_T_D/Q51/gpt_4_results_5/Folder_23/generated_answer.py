from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_pairs = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_lower = word.lower()
            anagram_pairs[tuple(sorted(word_lower))].append(word_lower)
    count = 0
    for value in anagram_pairs.values():
        size = len(value)
        if size > 1:
            count += size * (size - 1) // 2
    return count <= 49