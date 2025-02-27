def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 56:
        return substrings
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56 and substring not in substrings:
            substrings.append(substring)
    return substrings