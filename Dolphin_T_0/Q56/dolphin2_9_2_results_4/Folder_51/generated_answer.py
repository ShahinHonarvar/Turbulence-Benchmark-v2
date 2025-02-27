def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    n = len(set(s))
    if n < 96:
        return []
    substrings = []
    for i in range(len(s) - 96):
        substr = s[i:i + 96]
        if len(set(substr)) == 96:
            substrings.append(substr)
    return substrings