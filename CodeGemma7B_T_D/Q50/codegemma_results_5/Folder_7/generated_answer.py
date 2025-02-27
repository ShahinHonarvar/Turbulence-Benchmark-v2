def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        str_dict[string] = ''.join(sorted(string.lower()))
    count = 0
    for key, val in str_dict.items():
        if key != val:
            count += 1
            if count >= 178:
                return True
    return False