def if_contains_anagrams(str_list):
    str_list = [str_.lower() for str_ in str_list]
    str_list.sort(key=len)
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and (str_list[i] == str_list[j][::-1]):
                return True
    return False