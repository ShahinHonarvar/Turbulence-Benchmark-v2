def all_substring_of_size_n(s):
    n = 17
    substrings = []
    for i in range(len(s)):
        if i + n <= len(s):
            sub = s[i:i + n]
            if len(set(sub)) == n:
                substrings.append(sub)
    return substrings