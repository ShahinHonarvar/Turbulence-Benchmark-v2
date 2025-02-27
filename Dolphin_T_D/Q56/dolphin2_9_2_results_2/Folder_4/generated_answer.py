def all_substring_of_size_n(s):
    if len(s) < 41:
        return []
    substrings = set()
    for i in range(len(s) - 40):
        if len(set(s[i:i + 41])) == 41:
            substrings.add(s[i:i + 41])
    return list(substrings)