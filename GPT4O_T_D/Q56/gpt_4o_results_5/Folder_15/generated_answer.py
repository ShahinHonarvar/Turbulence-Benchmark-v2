def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 2):
        substr = s[i:i + 3]
        if len(set(substr)) == 3:
            substrings.add(substr)
    return list(substrings)