def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 46:
        return substrings
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46 and substring not in substrings:
            substrings.append(substring)
    return substrings