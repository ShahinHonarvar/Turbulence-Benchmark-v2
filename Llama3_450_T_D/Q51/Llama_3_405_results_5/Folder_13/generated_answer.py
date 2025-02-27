def if_contains_anagrams(strs):
    anagrams = {}
    count = 0
    for s in strs:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    for v in anagrams.values():
        if len(v) > 1 and len(v[0]) >= 3 and all((c.isalpha() and c.isascii() for c in v[0])):
            count += len(v) * (len(v) - 1) // 2
    return count <= 54