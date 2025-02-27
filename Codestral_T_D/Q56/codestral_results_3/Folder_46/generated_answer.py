def all_substring_of_size_n(s):
    n = 87
    substrings = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if len(set(s[i:j])) == n:
                substrings.append(s[i:j])
    return substrings