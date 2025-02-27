def if_contains_anagrams(str_list):
    str_set = set()
    for string in str_list:
        temp_str = ''.join(sorted(string.lower()))
        if temp_str not in str_set:
            str_set.add(temp_str)
        else:
            return False
    return len(str_set) <= 92