def all_substring_of_size_n(s):
    if len(s) < 77:
        return []
    sub_strings = set()
    for i in range(len(s) - 76):
        sub = s[i:i + 77]
        if len(sub) == 77 and len(set(sub)) == 77:
            sub_strings.add(sub)
    return list(sub_strings)