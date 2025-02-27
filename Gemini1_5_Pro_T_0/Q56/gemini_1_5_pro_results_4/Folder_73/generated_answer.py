def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 20:
        return substrings
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20 and substring not in substrings:
            substrings.append(substring)
    return substrings