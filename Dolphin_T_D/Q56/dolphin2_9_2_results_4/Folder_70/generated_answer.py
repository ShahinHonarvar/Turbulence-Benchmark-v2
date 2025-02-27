def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    substrings = set()
    for i in range(len(s) - 12):
        if len(set(s[i:i + 12])) == 12:
            substrings.add(s[i:i + 12])
    return list(substrings)