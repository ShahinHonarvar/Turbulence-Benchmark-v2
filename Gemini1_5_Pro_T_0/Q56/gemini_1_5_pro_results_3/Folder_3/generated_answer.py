def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 93:
        return substrings
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93:
            if substring not in substrings:
                substrings.append(substring)
    return substrings