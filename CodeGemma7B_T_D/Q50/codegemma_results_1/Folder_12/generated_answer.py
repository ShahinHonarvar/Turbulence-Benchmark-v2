def if_contains_anagrams(str_list):
    str_dict = {}
    for s in str_list:
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in str_dict:
            str_dict[s_sorted].append(s)
        else:
            str_dict[s_sorted] = [s]
    count = 0
    for k in str_dict.values():
        if len(k) >= 3:
            count += len(k) * (len(k) - 1) // 2
    return count >= 69