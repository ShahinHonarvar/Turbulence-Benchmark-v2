def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 21:
        return substrings
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21 and substring not in substrings:
            substrings.append(substring)
    return substrings