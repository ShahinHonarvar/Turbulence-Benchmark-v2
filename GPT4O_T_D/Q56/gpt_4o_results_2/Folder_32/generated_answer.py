def all_substring_of_size_n(s):
    if len(s) < 71:
        return []
    substrings = set()
    for i in range(len(s) - 70):
        substr = s[i:i + 71]
        if len(set(substr)) == 71:
            substrings.add(substr)
    return list(substrings)