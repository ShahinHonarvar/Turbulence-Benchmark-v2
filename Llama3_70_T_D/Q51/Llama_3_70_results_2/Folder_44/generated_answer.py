def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        key = ''.join(sorted(filter(str.isalpha, s_lower)))
        if len(key) < 3:
            continue
        if key in anagrams:
            anagrams[key].append(s_lower)
        else:
            anagrams[key] = [s_lower]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 75