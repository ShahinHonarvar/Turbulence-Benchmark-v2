def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 146:
        return substrings
    for i in range(len(s) - 146 + 1):
        substring = s[i:i + 146]
        if len(set(substring)) == 146:
            substrings.append(substring)
    return list(set(substrings))