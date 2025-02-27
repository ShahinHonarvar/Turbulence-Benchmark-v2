def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 94:
        return substrings
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(set(substring)) == 94 and substring not in substrings:
            substrings.append(substring)
    return substrings