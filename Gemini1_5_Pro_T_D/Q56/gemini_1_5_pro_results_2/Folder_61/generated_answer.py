def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) < 39:
        return sub_strings
    for i in range(len(s) - 38):
        sub_string = s[i:i + 39]
        if len(set(sub_string)) == 39:
            if sub_string not in sub_strings:
                sub_strings.append(sub_string)
    return sub_strings