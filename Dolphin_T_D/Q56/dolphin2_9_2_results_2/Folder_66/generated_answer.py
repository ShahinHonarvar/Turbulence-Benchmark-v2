def all_substring_of_size_n(input_str):
    substr_set = set()
    str_len = len(input_str)
    if str_len < 26:
        return []
    for i in range(str_len - 25):
        sub_str = input_str[i:i + 26]
        if len(set(sub_str)) == 26:
            substr_set.add(sub_str)
    return list(substr_set)