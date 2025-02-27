def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 69:
        return substrings
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if len(set(substring)) == 69:
            if substring not in substrings:
                substrings.append(substring)
    return substrings