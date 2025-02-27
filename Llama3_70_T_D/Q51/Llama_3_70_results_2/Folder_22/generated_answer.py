def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for s in lst:
        s_lower = s.lower()
        key = ''.join(sorted(s_lower))
        if len(key) >= 3 and key.isalpha():
            if key in anagrams:
                anagrams[key].append(s_lower)
            else:
                anagrams[key] = [s_lower]
    for v in anagrams.values():
        pairs += len(v) * (len(v) - 1) // 2
    return pairs <= 14