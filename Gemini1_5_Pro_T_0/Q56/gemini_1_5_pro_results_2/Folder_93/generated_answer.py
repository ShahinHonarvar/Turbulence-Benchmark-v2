def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 54:
        return substrings
    for i in range(len(s) - 53):
        substring = s[i:i + 54]
        if len(set(substring)) == 54 and substring not in substrings:
            substrings.append(substring)
    return substrings