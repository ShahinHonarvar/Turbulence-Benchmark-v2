def all_substring_of_size_n(s):
    if len(set(s)) != 26:
        return []
    substrings = set()
    for i in range(len(s) - 25):
        if len(set(s[i:i + 26])) == 26:
            substrings.add(s[i:i + 26])
    return list(substrings)