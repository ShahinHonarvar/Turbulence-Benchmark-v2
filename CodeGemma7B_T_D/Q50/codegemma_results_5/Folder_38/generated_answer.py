def if_contains_anagrams(str_list):
    str_map = {}
    for string in str_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            str_map.setdefault(sorted_string, []).append(string)
    for _, strings in str_map.items():
        if len(strings) >= 24:
            return True
    return False