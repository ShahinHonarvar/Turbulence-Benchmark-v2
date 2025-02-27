def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    count = 0
    for k in anagrams:
        count += len(anagrams[k]) * (len(anagrams[k]) - 1) // 2
    return count >= 40