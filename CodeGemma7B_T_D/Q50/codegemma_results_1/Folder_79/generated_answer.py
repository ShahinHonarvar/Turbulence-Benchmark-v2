def if_contains_anagrams(str_list):
    str_len_list = [len(s) for s in str_list if len(s) >= 3]
    str_len_list.sort()
    str_len_list = str_len_list[str_len_list.index(str_len_list[0]):]
    return True if len(str_len_list) / 2 >= 40 else False