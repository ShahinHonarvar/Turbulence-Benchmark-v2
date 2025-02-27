def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) < 67:
        return sub_strings
    for i in range(len(s) - 66):
        sub_string = s[i:i + 67]
        if len(set(sub_string)) == 67:
            if sub_string not in sub_strings:
                sub_strings.append(sub_string)
    return sub_strings