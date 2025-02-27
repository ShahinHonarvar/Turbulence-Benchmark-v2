def all_substring_of_size_n(s):
    n = 57
    substrings = []
    if n > len(s) or len(set(s)) < n:
        return substrings
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))