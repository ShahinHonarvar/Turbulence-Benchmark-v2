def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join(filter(lambda c: c.isalpha(), s)).lower()
        if len(s) < 3:
            continue
        k = ''.join(sorted(s))
        if k in anagrams:
            anagrams[k] += 1
        else:
            anagrams[k] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 65