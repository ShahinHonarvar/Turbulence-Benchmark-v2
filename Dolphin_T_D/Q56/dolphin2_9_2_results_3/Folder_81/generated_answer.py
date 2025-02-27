def all_substring_of_size_n(s):
    if not s:
        return []
    n = 98
    substrings = {}
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings[sub] = 1
    return list(substrings.keys())