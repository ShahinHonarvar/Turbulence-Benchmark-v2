def if_contains_anagrams(lst):
    pairs = 0
    s = set([''.join(sorted(w.lower()[:3])) for w in lst])
    for w in lst:
        if len(w) >= 3:
            for ww in s:
                if ww == ''.join(sorted(w.lower()[:3])):
                    pairs += 1
    return pairs / 2 <= 279