def all_substring_of_size_n(s):
    if len(s) < 77:
        return []
    substrings = []
    for i in range(len(s) - 76):
        substr = s[i:i + 77]
        if len(set(substr)) == 77:
            substrings.append(substr)
    return substrings