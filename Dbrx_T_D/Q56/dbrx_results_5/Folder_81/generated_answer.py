def all_substring_of_size_n(s):
    n = 98
    if len(s) < n:
        return []
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        substrings.add(substring)
    return list(substrings)