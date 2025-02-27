def all_substring_of_size_n(s):
    substrings = set()
    n = 40
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)