def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 50:
        return substrings
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50:
            substrings.append(substring)
    return substrings