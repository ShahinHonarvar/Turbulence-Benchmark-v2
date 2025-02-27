from collections import Counter

def if_contains_anagrams(lst):
    count = Counter(lst)
    result = {tuple(sorted(k.lower())): v for k, v in count.items() if len(k) >= 3}
    return len([1 for v in result.values() if v > 1]) <= 34