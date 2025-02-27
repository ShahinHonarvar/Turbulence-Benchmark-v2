def if_contains_anagrams(str_list):
    str_set = set()
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower().replace(' ', '')))
        if len(sorted_string) < 3:
            continue
        if sorted_string in str_set:
            return False
        str_set.add(sorted_string)
    return True