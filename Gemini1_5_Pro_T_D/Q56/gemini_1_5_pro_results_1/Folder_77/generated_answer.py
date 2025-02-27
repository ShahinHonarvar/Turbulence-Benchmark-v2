def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 144:
        return substrings
    for i in range(len(s) - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            if substring not in substrings:
                substrings.append(substring)
    return substrings