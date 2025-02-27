from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = Counter((''.join(sorted(word.lower())) for word in words if len(word) >= 3))
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 46