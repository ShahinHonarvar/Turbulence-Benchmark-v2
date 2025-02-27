def all_substring_of_size_n(s):
    n = 53
    substrings = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            subs = s[i:j]
            if len(set(subs)) == n:
                substrings.append(subs)
    return substrings