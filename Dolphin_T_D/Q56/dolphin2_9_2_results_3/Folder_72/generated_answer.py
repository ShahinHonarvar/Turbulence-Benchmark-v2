def all_substring_of_size_n(s):
    n = 88
    if len(s) < n:
        return []
    sub_strings = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            sub_strings.add(substr)
    return list(sub_strings)