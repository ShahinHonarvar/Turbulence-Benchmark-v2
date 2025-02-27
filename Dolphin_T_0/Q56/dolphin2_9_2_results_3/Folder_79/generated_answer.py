def all_substring_of_size_n(s):
    n = 61
    if len(s) < n:
        return []
    return [s[i:n + i] for i in range(len(s) - n + 1)]