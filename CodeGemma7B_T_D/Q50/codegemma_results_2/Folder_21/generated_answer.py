def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if len(s) >= 3 and sorted_s in str_dict:
            str_dict[sorted_s] += 1
        else:
            str_dict[sorted_s] = 1
    pairs = 0
    for count in str_dict.values():
        pairs += count * (count - 1) // 2
    return pairs >= 136