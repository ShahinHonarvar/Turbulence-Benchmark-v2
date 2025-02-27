def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 71:
        return substrings
    for i in range(len(s) - 70):
        substring = s[i:i + 71]
        if len(set(substring)) == 71 and substring not in substrings:
            substrings.append(substring)
    return substrings