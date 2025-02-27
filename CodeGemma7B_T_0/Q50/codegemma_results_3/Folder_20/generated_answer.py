def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    anagram_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    if len([v for v in anagram_dict.values() if len(v) >= 64]) > 0:
        return True
    return False