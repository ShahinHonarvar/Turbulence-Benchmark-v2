def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 16 + 1):
        substr = s[i:i + 16]
        if len(set(substr)) == 16:
            substrings.add(substr)
    return list(substrings)