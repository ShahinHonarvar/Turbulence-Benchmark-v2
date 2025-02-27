def all_substring_of_size_n(s):
    n = 88
    unique_substrings = set()
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            unique_substrings.add(substr)
    return list(unique_substrings)