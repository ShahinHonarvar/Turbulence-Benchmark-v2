def if_contains_anagrams(strings):
    anagrams_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams_dict:
            anagrams_dict[sorted_s].append(s)
        else:
            anagrams_dict[sorted_s] = [s]
    count = sum((1 for v in anagrams_dict.values() if len(v) > 1))
    return count >= 18