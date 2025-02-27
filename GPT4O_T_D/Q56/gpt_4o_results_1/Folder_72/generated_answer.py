def all_substring_of_size_n(s):
    if len(s) < 88:
        return []
    substrings = set()
    for i in range(len(s) - 87):
        substr = s[i:i + 88]
        if len(set(substr)) == 88:
            substrings.add(substr)
    return list(substrings)