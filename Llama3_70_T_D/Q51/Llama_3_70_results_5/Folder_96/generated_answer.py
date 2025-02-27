def if_contains_anagrams(lst):
    anagrams_dict = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams_dict:
            anagrams_dict[sorted_s].append(s)
        else:
            anagrams_dict[sorted_s] = [s]
    anagrams_count = sum((1 for v in anagrams_dict.values() if len(v) > 1))
    return anagrams_count <= 2