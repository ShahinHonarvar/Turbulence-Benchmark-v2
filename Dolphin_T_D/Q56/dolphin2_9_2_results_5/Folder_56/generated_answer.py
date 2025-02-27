def all_substring_of_size_n(s):
    if len(s) < 69:
        return []
    substrings = set()
    for i in range(len(s) - 68):
        sub = s[i:i + 69]
        substrings.add(sub)
    return list(substrings)