def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str not in str_dict:
            str_dict[sorted_str] = string
        elif len(str_dict) > 25:
            return False
    return True