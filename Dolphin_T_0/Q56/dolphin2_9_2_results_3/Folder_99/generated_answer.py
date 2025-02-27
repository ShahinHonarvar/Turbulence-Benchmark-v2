def all_substring_of_size_n(s):
    if len(s) < 110:
        return []
    substrings = []
    for i in range(len(s) - 110 + 1):
        sub = s[i:i + 110]
        if len(set(sub)) == 110:
            substrings.append(sub)
    return substrings