def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    substrings = []
    for i in range(len(s) - 8):
        substr = s[i:i + 9]
        if len(set(substr)) == 9:
            substrings.append(substr)
    return substrings