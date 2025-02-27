def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 36:
        return substrings
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(set(substring)) == 36:
            if substring not in substrings:
                substrings.append(substring)
    return substrings