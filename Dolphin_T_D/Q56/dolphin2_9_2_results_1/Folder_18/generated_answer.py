def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    substrings = []
    for i in range(len(s) - 62):
        if len(set(s[i:i + 63])) == len(s[i:i + 63]):
            substrings.append(s[i:i + 63])
    if substrings:
        return substrings
    else:
        return []