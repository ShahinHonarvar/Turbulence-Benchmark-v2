def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            s_sorted = ''.join(sorted(s_lower))
            if s_sorted in anagrams:
                count += len(anagrams[s_sorted])
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
    return count <= 188 * 2