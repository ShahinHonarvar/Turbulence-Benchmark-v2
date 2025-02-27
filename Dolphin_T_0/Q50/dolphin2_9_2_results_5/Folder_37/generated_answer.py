from collections import Counter

def if_contains_anagrams(words):
    counter = Counter((word.lower() for word in words if len(word) >= 3))
    anagram_pairs = sum((n * (n - 1) // 2 for n in counter.values() if n > 1))
    return anagram_pairs >= 29