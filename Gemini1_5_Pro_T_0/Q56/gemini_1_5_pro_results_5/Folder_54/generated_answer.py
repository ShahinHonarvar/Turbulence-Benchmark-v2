def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 28:
        return substrings
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(set(substring)) == 28 and substring not in substrings:
            substrings.append(substring)
    return substrings