def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in str_dict:
            str_dict[sorted_string] += 1
            if str_dict[sorted_string] > 113:
                return False
        else:
            str_dict[sorted_string] = 1
    return True