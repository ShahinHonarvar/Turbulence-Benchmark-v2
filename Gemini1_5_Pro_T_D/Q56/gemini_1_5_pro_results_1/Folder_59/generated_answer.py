def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 77:
        return substrings
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if len(set(substring)) == 77 and substring not in substrings:
            substrings.append(substring)
    return substrings