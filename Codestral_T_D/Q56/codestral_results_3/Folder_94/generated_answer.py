def all_substring_of_size_n(s):
    n = 70
    substrings = []
    for i in range(len(s)):
        for j in range(i + n, i + n + 1):
            substring = s[i:j]
            if len(substring) == len(set(substring)) == n:
                substrings.append(substring)
    return substrings