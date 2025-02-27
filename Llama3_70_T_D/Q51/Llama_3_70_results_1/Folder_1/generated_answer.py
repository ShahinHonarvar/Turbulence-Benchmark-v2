def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_dict = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams_dict:
            anagrams_count += len(anagrams_dict[s_sorted])
            anagrams_dict[s_sorted].append(s)
        else:
            anagrams_dict[s_sorted] = [s]
    return anagrams_count <= 30