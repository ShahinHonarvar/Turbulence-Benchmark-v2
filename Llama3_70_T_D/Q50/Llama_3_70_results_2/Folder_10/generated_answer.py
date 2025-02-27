def if_contains_anagrams(lst):
    anagrams = {}
    pairs = set()
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            for anagram in anagrams[sorted_s]:
                pairs.add(tuple(sorted([anagram, s])))
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return len(pairs) >= 52