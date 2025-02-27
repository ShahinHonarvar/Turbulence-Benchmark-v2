def if_contains_anagrams(str_list):
    str_dict = {}
    count = 0
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if s in str_dict:
            if str_dict[s] >= 3:
                count += 1
            else:
                count += 2
            str_dict[s] += 1
        else:
            str_dict[s] = 1
    return count <= 131