def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            str_dict[string] = str_dict.get(string, 0) + 1
    pairs = 0
    for count in str_dict.values():
        pairs += count * (count - 1) // 2
    return pairs <= 54