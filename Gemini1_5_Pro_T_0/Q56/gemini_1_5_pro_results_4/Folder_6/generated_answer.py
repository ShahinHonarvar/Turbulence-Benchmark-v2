def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 23:
        return substrings
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            substrings.append(substring)
    return set(substrings)