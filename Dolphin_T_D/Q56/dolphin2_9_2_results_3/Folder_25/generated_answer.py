def all_substring_of_size_n(input_string):
    size_n = 67
    sub_strings = []
    for i in range(len(input_string) - size_n + 1):
        sub_string = input_string[i:i + size_n]
        if len(set(sub_string)) == len(sub_string) and sub_string not in sub_strings:
            sub_strings.append(sub_string)
    if not sub_strings:
        return []
    else:
        return sub_strings