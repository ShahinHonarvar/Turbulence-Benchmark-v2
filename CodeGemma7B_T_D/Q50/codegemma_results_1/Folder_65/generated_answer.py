def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_dict = {}
    for str in str_list:
        sorted_str = ''.join(sorted(str))
        if sorted_str not in str_dict:
            str_dict[sorted_str] = 1
        else:
            str_dict[sorted_str] += 1
    for count in str_dict.values():
        if count >= 94:
            return True
    return False