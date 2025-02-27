def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 33):
        substr = s[i:i + 34]
        if len(set(substr)) == 34:
            substrings.add(substr)
    return list(substrings)