def all_substring_of_size_n(s):
    sub_strings = set()
    for i in range(len(s) - 24):
        string_of_interest = s[i:i + 25]
        if len(set(string_of_interest)) == 25:
            sub_strings.add(string_of_interest)
    return list(sub_strings)