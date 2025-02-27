def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) < 18:
        return sub_strings
    for i in range(len(s) - 17):
        sub_string = s[i:i + 18]
        if len(set(sub_string)) == 18:
            if sub_string not in sub_strings:
                sub_strings.append(sub_string)
    return sub_strings