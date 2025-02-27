def all_substring_of_size_n(s):
    n = 37
    substrings = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if len(sub) == len(set(sub)):
                substrings.append(sub)
    return substrings