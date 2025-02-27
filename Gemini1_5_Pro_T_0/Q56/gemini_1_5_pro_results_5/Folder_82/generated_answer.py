def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 100:
        return substrings
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if len(set(substring)) == 100:
            substrings.append(substring)
    return list(set(substrings))