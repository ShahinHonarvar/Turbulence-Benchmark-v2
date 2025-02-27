def if_contains_anagrams(str_list):
    str_set = set()
    for str in str_list:
        str = str.lower()
        str_sorted = ''.join(sorted(str))
        if len(str) >= 3:
            if str_sorted in str_set:
                str_set.add(str_sorted)
            else:
                str_set.add(str_sorted)
    if len(str_set) >= 55:
        return True
    else:
        return False