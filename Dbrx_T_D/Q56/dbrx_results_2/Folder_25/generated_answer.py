def all_substring_of_size_n(s):
    n = 67
    substrings = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) != n:
            continue
        if len(set(substring)) != n:
            continue
        if substring not in substrings:
            substrings.append(substring)
    return substrings