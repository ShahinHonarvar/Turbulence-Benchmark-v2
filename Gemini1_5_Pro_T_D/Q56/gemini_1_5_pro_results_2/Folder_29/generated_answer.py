def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 95:
        return substrings
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(set(substring)) == 95:
            if substring not in substrings:
                substrings.append(substring)
    return substrings