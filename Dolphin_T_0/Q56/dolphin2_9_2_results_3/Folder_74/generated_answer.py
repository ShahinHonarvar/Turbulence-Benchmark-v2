def all_substring_of_size_n(s):
    n = len(s)
    if n <= 96:
        return []
    substrings = set()
    for i in range(n - 96):
        sub = s[i:i + 97]
        if len(set(sub)) == 97:
            substrings.add(sub)
    return list(substrings)