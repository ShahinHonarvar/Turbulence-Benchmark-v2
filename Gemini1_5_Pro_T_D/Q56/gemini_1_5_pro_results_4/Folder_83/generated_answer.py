def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 48:
        return substrings
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if len(set(substring)) == 48 and substring not in substrings:
            substrings.append(substring)
    return substrings