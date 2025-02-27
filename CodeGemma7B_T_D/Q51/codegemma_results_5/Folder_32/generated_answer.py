def if_contains_anagrams(str_list):
    str_set = set()
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in str_set:
            return False
        str_set.add(sorted_str)
    return True