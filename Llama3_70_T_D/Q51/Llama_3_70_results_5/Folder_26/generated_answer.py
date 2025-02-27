def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 35