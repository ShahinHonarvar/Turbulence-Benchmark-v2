def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if s.isalpha() and len(s) >= 3]
    anagrams = {}
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return count <= 28