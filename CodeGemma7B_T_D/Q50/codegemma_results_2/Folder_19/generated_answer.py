def if_contains_anagrams(str_list):
    str_lowers = [str_.lower() for str_ in str_list if len(str_) >= 3]
    lower_set = set(str_lowers)
    pair_count = 0
    for str_ in lower_set:
        str_count = str_lowers.count(str_)
        pair_count += str_count * (str_count - 1) // 2
    return pair_count >= 84