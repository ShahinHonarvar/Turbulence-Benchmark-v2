def all_substring_of_size_n(input_str):
    n = 144
    sub_strings = set()
    for i in range(len(input_str) - n + 1):
        if len(set(input_str[i:i + n])) == n:
            sub_strings.add(input_str[i:i + n])
    return list(sub_strings)