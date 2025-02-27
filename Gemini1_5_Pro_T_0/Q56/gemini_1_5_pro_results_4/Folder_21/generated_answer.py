def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 106:
        return substrings
    for i in range(len(s) - 105):
        substring = s[i:i + 106]
        if len(set(substring)) == 106:
            substrings.append(substring)
    return set(substrings)