def if_contains_anagrams(str_list):
    str_dict = {}
    pairs = 0
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str not in str_dict:
            str_dict[sorted_str] = set()
        str_dict[sorted_str].add(string)
    for values in str_dict.values():
        pairs += len(values) * (len(values) - 1) // 2
    return pairs >= 21