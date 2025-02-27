def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) < 3:
            continue
        s = s.lower()
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].add(s)
        else:
            anagrams[key] = {s}
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 14