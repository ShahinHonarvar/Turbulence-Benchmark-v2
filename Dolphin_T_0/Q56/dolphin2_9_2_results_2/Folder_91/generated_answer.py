def all_substring_of_size_n(s):
    n = 6
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)