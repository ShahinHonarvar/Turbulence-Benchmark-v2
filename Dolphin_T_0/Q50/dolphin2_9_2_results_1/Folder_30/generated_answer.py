from collections import Counter

def if_contains_anagrams(lst):
    count = sum((1 for word in lst if len(word) >= 3 for a, b in zip(word.lower(), word.lower()[::-1]) if a == b or a != b))
    return count >= 78 * 2