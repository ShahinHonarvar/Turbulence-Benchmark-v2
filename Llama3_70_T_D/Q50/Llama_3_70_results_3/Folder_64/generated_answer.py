def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s_lower) >= 3 and sorted_str in anagrams:
            count += 1
        anagrams[sorted_str] = True
    return count >= 5