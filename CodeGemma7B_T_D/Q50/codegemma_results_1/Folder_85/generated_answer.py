def if_contains_anagrams(str_list):
    str_dict = {}
    str_list = [sorted(s.lower()) for s in str_list]
    for s in str_list:
        str_dict.setdefault(''.join(s), []).append(s)
    if sum((len(v) >= 3 for v in str_dict.values())) >= 73:
        return True
    else:
        return False