def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    n = 36
    sub_strings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            sub_strings.add(sub)
    return list(sub_strings)