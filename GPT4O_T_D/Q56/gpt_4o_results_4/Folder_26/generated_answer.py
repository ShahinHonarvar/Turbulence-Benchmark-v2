def all_substring_of_size_n(s):
    if len(s) < 33:
        return []
    substrings = set()
    for i in range(len(s) - 32):
        substr = s[i:i + 33]
        if len(substr) == 33 and len(set(substr)) == 33:
            substrings.add(substr)
    return list(substrings)