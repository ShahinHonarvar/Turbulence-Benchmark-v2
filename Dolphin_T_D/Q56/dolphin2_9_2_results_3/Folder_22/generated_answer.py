def all_substring_of_size_n(s):
    if len(s) < 22:
        return []
    substrings = set()
    for i in range(len(s) - 21):
        substr = s[i:i + 22]
        if len(set(substr)) == len(substr):
            substrings.add(substr)
    return list(substrings)