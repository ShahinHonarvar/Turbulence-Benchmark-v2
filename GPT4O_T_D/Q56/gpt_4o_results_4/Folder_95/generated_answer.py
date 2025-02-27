def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    substrings = set()
    n = len(s)
    for i in range(n - 88):
        substring = s[i:i + 89]
        if len(set(substring)) == 89:
            substrings.add(substring)
    return list(substrings)