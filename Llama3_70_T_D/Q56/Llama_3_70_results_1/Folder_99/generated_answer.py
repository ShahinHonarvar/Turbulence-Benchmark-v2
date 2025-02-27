def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 110 + 1):
        substring = s[i:i + 110]
        if len(set(substring)) == 110:
            substrings.add(substring)
    return list(substrings)