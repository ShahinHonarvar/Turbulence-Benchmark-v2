def all_substring_of_size_n(s):
    n = 20
    substrings = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == n:
                substrings.append(substring)
    return substrings