def all_substring_of_size_n(s):
    if len(set(s)) < 97:
        return []
    sub_strings = set()
    for i in range(len(s) - 96):
        sub_strings.add(s[i:i + 97])
    return list(sub_strings)