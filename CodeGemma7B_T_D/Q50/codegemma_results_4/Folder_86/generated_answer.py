def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_dict = {}
    for str in str_list:
        if len(str) >= 3:
            sorted_str = ''.join(sorted(str))
            if sorted_str in str_dict:
                str_dict[sorted_str] += 1
            else:
                str_dict[sorted_str] = 1
    num_pairs = 0
    for value in str_dict.values():
        if value >= 2:
            num_pairs += value * (value - 1) // 2
    return num_pairs >= 115