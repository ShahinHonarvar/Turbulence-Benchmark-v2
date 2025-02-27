def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string not in str_dict:
            str_dict[sorted_string] = string
    if len(str_dict) <= 366:
        return True
    else:
        return False