def if_contains_anagrams(str_list):
    str_set = set()
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower()))
        str_set.add((sorted_str, str))
    count = 0
    for key, str_list in str_set.items():
        if len(str_list) >= 89:
            count += len(str_list) - 89
    return count >= 8900