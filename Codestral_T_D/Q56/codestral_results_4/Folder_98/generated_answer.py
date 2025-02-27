def all_substring_of_size_n(s):
    n = 10
    substrings = []
    for i in range(len(s)):
        sub = s[i:i + n]
        if len(sub) == n and len(set(sub)) == n:
            substrings.append(sub)
    return substrings