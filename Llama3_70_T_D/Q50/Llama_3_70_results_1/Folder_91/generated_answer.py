def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s_lower)
        else:
            anagrams[s_sorted] = [s_lower]
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count >= 6