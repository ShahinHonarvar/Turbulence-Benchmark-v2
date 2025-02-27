def if_contains_anagrams(str_list):
    str_dict = {}
    for s in str_list:
        sl = ''.join(sorted(s.lower()))
        if sl in str_dict:
            str_dict[sl] += 1
        else:
            str_dict[sl] = 1
    pair_count = 0
    for count in str_dict.values():
        pair_count += count * (count - 1) // 2
    return pair_count <= 35