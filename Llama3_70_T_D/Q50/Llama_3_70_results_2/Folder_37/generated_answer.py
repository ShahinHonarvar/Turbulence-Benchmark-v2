def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        if len(s) >= 3:
            s_lower = s.lower()
            s_sorted = ''.join(sorted(s_lower))
            if s_sorted in anagrams:
                count += len(anagrams[s_sorted])
                anagrams[s_sorted].append(s_lower)
            else:
                anagrams[s_sorted] = [s_lower]
    return count >= 29