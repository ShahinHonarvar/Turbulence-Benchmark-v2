def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = s.lower()
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    for c in anagrams.values():
        count += c * (c - 1) // 2
    return count <= 279