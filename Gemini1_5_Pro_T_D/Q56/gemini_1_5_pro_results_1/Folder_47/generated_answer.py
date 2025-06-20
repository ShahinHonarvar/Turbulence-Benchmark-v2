def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 91:
        return substrings
    for i in range(len(s) - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91:
            substrings.append(substring)
    return list(set(substrings))