def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) < 45:
        return sub_strings
    for i in range(len(s) - 44):
        sub_string = s[i:i + 45]
        if len(set(sub_string)) == 45 and sub_string not in sub_strings:
            sub_strings.append(sub_string)
    return sub_strings