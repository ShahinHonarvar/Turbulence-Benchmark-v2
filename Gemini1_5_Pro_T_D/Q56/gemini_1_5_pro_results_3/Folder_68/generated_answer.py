def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 75:
        return substrings
    for i in range(len(s) - 74):
        substring = s[i:i + 75]
        if len(set(substring)) == 75:
            if substring not in substrings:
                substrings.append(substring)
    return substrings