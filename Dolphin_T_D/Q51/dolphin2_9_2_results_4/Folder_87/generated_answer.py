from collections import Counter

def if_contains_anagrams(lst):
    result = False
    pairs = set()
    counter = Counter(lst)
    for key in counter:
        sorted_key = ''.join(sorted(key.lower()))
        if len(sorted_key) >= 3:
            if sorted_key in counter:
                pairs.add(sorted_key)
    return len(pairs) <= 392