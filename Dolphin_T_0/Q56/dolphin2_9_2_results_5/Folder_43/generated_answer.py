def all_substring_of_size_n(s):
    substrings = set()
    n = 86
    for i in range(0, len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)