def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 85:
        return substrings
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(set(substring)) == 85 and substring not in substrings:
            substrings.append(substring)
    return substrings