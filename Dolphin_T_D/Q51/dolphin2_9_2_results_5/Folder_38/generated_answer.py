from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        c.update(Counter(word.lower()))
    d = {k: v // 2 for k, v in c.items() if v >= 2 and len(k) >= 3}
    return len(d) >= 416