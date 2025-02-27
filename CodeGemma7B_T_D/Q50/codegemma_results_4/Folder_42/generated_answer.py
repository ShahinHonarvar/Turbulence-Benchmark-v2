def if_contains_anagrams(str_list):
    str_dict = {}
    for str in str_list:
        str = sorted(str.lower())
        str = ''.join(str)
        if len(str) < 3:
            continue
        if str not in str_dict:
            str_dict[str] = [str]
        else:
            str_dict[str].append(str)
    return len([str_list for str_list in str_dict.values() if len(str_list) >= 233]) > 0