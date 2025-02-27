def all_substring_of_size_n(s):
    substrings = []
    n = 39
    if len(s) < n:
        return substrings
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))