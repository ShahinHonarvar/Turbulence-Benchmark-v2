def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        string = string.lower()
        sorted_str = ''.join(sorted(string))
        if len(string) >= 3 and sorted_str in str_dict:
            str_dict[sorted_str] += 1
            if str_dict[sorted_str] >= 75:
                return True
        elif len(string) >= 3:
            str_dict[sorted_str] = 1
    return False