from collections import Counter

def if_contains_anagrams(words):
    anagrams_counts = [Counter((word.lower() for word in words if len(word) >= 3)) - Counter({c: 26 for c in 'abcdefghijklmnopqrstuvwxyz'})]
    return max(anagrams_counts.values()) <= 36