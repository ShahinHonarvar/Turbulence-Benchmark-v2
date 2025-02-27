def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 110:
        return substrings
    for i in range(len(s) - 109):
        substring = s[i:i + 110]
        if len(set(substring)) == 110 and substring not in substrings:
            substrings.append(substring)
    return substrings