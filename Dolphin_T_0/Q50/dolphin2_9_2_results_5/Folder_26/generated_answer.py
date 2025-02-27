from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):
    anagram_counter = Counter()
    for word in words:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            anagram_counter[word_sorted] += 1
    count = sum((c * (c - 1) // 2 for c in anagram_counter.values() if c >= 2))
    return count >= 49