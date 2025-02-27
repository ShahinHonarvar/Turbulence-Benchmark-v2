def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        s_filtered = ''.join(filter(str.isalpha, s_lower))
        if len(s_filtered) < 3:
            continue
        sorted_s = ''.join(sorted(s_filtered))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s_lower)
        else:
            anagrams[sorted_s] = [s_lower]
    pairs = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return pairs <= 85