def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 87:
        return substrings
    for i in range(len(s) - 86):
        substring = s[i:i + 87]
        if len(set(substring)) == 87 and substring not in substrings:
            substrings.append(substring)
    return substrings