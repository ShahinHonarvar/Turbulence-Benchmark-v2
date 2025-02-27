def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 120:
        return substrings
    for i in range(len(s) - 120 + 1):
        substring = s[i:i + 120]
        if len(set(substring)) == 120 and substring not in substrings:
            substrings.append(substring)
    return substrings