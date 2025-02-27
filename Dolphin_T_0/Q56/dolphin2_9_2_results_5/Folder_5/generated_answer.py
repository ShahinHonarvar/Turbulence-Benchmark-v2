def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 63):
        substr = s[i:i + 64]
        if len(set(substr)) == 64:
            substrings.add(substr)
    return list(substrings)