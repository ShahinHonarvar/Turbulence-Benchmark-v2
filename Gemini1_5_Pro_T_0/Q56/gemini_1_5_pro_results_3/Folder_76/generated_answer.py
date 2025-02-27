def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 149:
        return substrings
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149:
            substrings.append(substring)
    return set(substrings)