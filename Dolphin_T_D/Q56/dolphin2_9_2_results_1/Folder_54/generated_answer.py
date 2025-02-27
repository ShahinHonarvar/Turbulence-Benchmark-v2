def all_substring_of_size_n(s):
    if len(s) < 28:
        return []
    substrings = []
    for i in range(len(s)):
        if len(set(s[i:i + 28])) == 28:
            substrings.append(s[i:i + 28])
    return substrings