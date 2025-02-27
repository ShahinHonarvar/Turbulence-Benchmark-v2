def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_dict = {}
    for s in lst:
        s_lower = ''.join(sorted(s.casefold()))
        if s_lower in anagrams_dict:
            anagrams_dict[s_lower] += 1
        else:
            anagrams_dict[s_lower] = 2
    for value in anagrams_dict.values():
        if value > 1:
            anagrams_count += value // 2
            if anagrams_count > 26:
                return False
    return True