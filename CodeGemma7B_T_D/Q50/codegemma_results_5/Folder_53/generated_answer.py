def if_contains_anagrams(str_list):
    str_dict = {}
    str_pairs = 0
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if key in str_dict:
            str_dict[key].append(s)
        else:
            str_dict[key] = [s]
    for key, anagrams in str_dict.items():
        if len(anagrams) >= 3:
            str_pairs += len(anagrams)
    return str_pairs >= 11