def all_substring_of_size_n(s):
    if len(s) < 40:
        return []
    substrings = []
    for i in range(len(s) - 39):
        if len(set(s[i:i + 40])) == 40:
            substrings.append(s[i:i + 40])
    return substrings