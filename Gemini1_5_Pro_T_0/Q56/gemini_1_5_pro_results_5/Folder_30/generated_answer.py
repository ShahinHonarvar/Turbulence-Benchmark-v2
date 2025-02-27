def all_substring_of_size_n(s):
    sub_strings = []
    if len(s) < 79:
        return sub_strings
    for i in range(len(s) - 78):
        substring = s[i:i + 79]
        if len(set(substring)) == 79 and substring not in sub_strings:
            sub_strings.append(substring)
    return sub_strings