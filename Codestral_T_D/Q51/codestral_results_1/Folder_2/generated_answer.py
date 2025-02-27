from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter((''.join(sorted(word.lower())) for word in lst if len(word) >= 3))
    anagram_pairs = sum((n * (n - 1) for n in counter.values()))
    return anagram_pairs <= 81