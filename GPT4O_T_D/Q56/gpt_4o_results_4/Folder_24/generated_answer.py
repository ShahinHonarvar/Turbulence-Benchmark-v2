def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    if n < 52:
        return []
    for i in range(n - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            substrings.add(substring)
    return list(substrings)