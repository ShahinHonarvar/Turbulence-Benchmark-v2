def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 25:
        return substrings
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            substrings.append(substring)
    return substrings