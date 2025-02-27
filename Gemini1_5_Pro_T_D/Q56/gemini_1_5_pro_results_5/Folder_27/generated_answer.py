def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 57:
        return substrings
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if len(set(substring)) == 57:
            if substring not in substrings:
                substrings.append(substring)
    return substrings