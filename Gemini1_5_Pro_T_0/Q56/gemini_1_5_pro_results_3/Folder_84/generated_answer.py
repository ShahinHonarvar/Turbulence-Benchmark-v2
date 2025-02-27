def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 114:
        return substrings
    for i in range(len(s) - 113):
        substring = s[i:i + 114]
        if len(set(substring)) == 114 and substring not in substrings:
            substrings.append(substring)
    return substrings