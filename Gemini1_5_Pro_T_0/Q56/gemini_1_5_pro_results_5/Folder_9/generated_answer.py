def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 34:
        return substrings
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(set(substring)) == 34:
            if substring not in substrings:
                substrings.append(substring)
    return substrings