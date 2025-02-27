def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 124:
        return substrings
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        if len(set(substring)) == 124 and substring not in substrings:
            substrings.append(substring)
    return substrings