from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for pair in lst:
        if len(pair) < 3:
            continue
        c = Counter(pair.lower())
        for o in lst:
            if len(o) < 3 or o == pair:
                continue
            if c == Counter(o.lower()):
                pairs += 1
                lst.remove(o)
                break
    return pairs >= 38