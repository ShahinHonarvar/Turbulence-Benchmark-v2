def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) >= 28:
        for i in range(len(s) - 27):
            sub_string = s[i:i + 28]
            if len(set(sub_string)) == 28 and sub_string not in sub_strings:
                sub_strings.append(sub_string)
    return sub_strings