def if_contains_anagrams(s_list):
    an_dict = {}
    for s in s_list:
        if len(s) >= 3:
            s = s.lower()
            s_list = sorted(s)
            key = ''.join(s_list)
            if key in an_dict.keys():
                an_dict[key] += 1
            else:
                an_dict[key] = 1
    count = 0
    for k, v in an_dict.items():
        count += v * (v - 1) // 2
    if count >= 123:
        return True
    else:
        return False