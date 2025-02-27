def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 92:
        return substrings
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            if substring not in substrings:
                substrings.append(substring)
    return substrings