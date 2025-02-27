def if_contains_anagrams(str_list):
    str_list.sort(key=len, reverse=False)
    return len(str_list) >= 42