def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    pairs = 0
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            count += 1
            anagrams[sorted_str].append(s_lower)
        else:
            anagrams[sorted_str] = [s_lower]
    for v in anagrams.values():
        if len(v) > 1:
            pairs += len(v) * (len(v) - 1) // 2
    return pairs <= 65