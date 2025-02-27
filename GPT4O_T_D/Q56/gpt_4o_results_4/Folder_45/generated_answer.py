def all_substring_of_size_n(s):
    n = 29
    if len(s) < n:
        return []
    substrings = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == len(set(substr)):
            substrings.add(substr)
    return list(substrings)