def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 22):
        substr = s[i:i + 23]
        if len(set(substr)) == 23:
            substrings.add(substr)
    return list(substrings)