def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 68:
        return substrings
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            if substring not in substrings:
                substrings.append(substring)
    return substrings