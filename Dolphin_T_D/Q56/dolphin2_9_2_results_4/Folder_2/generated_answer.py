def all_substring_of_size_n(s):
    n = 56
    if len(s) < n:
        return []
    substrings = set()
    for i in range(len(s) - n + 1):
        chunk = s[i:i + n]
        if len(set(chunk)) == n:
            substrings.add(chunk)
    return list(substrings)