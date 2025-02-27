def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 49:
        return substrings
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if len(set(substring)) == 49:
            if substring not in substrings:
                substrings.append(substring)
    return substrings