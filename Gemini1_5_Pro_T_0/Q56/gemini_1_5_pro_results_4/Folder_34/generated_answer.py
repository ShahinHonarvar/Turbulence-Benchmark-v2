def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 84:
        return substrings
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if len(set(substring)) == 84:
            substrings.append(substring)
    return list(set(substrings))