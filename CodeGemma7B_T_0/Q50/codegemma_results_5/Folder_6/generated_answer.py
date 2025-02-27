def if_contains_anagrams(str_list):
    str_list = [str_.lower() for str_ in str_list]
    str_list = [str_ for str_ in str_list if len(str_) >= 3]
    str_list.sort()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                return True
    return False