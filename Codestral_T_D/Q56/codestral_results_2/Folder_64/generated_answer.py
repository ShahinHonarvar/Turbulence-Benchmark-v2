def all_substring_of_size_n(s):
    n = 8
    substrings = set()
    for i in range(len(s)):
        sub = s[i:i + n]
        if len(sub) == n and len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)