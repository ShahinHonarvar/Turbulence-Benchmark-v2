def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    substrings = set()
    for i in range(0, len(s) - 23):
        if len(set(s[i:i + 24])) == 24:
            substrings.add(s[i:i + 24])
    return list(substrings)