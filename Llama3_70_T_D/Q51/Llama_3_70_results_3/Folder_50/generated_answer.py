def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_dict = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_lower = ''.join((c for c in s_lower if c.isalpha()))
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagrams_dict:
            anagrams_count += len(anagrams_dict[sorted_str])
            anagrams_dict[sorted_str].append(s)
        else:
            anagrams_dict[sorted_str] = [s]
    return anagrams_count <= 47