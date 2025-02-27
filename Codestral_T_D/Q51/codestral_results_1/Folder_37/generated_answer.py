from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = Counter((tuple(sorted(word.lower())) for word in lst if len(word) >= 3))
    return sum((count * (count - 1) for count in anagram_counts.values())) <= 206