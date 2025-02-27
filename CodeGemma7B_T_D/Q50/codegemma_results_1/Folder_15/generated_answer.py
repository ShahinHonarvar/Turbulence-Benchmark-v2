def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in str_dict:
            str_dict[sorted_string] += 1
            if str_dict[sorted_string] >= 4:
                return True
        else:
            str_dict[sorted_string] = 1
    return False