def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 19):
        substr = s[i:i + 20]
        if len(substr) == 20 and len(set(substr)) == 20:
            substrings.add(substr)
    return list(substrings)