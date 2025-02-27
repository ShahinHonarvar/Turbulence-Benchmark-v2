def all_substring_of_size_n(s):
    n = 89
    if len(s) < n:
        return []
    substr_set = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substr_set.add(substring)
    return list(substr_set)