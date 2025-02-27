def all_substring_of_size_n(s):
    result = []
    n = 22
    if len(s) < n:
        return result
    substrings = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == n:
            substrings.add(substr)
    return list(substrings)