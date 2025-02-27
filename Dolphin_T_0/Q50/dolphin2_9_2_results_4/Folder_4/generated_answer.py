from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter((word.lower() for word in lst if len(word) >= 3))
    return len([item for item in counter.values() if item >= 2]) >= 42