def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = {}
    for s in str_list:
        key = ''.join(sorted(s))
        if key in str_dict:
            str_dict[key].append(s)
        else:
            str_dict[key] = [s]
    return len([anagrams for anagrams in str_dict.values() if len(anagrams) >= 78]) >= 1