def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 10):
        substr = s[i:i + 11]
        if len(set(substr)) == 11:
            substrings.add(substr)
    return list(substrings)