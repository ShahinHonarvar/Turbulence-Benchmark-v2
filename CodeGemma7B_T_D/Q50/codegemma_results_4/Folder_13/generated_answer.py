def if_contains_anagrams(str_list):
    str_dict = {}
    count = 0
    for s in str_list:
        b = ''.join(sorted(s.lower()))
        if b in str_dict:
            str_dict[b] += 1
        else:
            str_dict[b] = 1
    for c in str_dict.values():
        if c >= 144:
            return True
    return False