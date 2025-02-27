def has_at_least_44_anagrams(str_list):
    str_list = [s.lower() for s in str_list if len(s) >= 3]
    str_dict = {}
    for s in str_list:
        sorted_str = ''.join(sorted(s))
        str_dict.setdefault(sorted_str, []).append(s)
    for l in str_dict.values():
        if len(l) >= 44:
            return True
    return False