def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 89:
        return substrings
    for i in range(len(s) - 88):
        substring = s[i:i + 89]
        if len(set(substring)) == 89:
            substrings.append(substring)
    return list(set(substrings))