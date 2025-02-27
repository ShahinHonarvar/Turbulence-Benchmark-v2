from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    pairs = set()
    for word in lst:
        counter = Counter(word)
        for ch in word:
            counter[ch] -= 1
            pairs.add(tuple(counter.values()))
    return len(pairs) <= 34