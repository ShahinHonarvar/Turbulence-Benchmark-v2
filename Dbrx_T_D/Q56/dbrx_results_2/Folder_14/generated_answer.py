def all_substring_of_size_n(s):
    n = 85
    if len(s) < n or len(set(s)) < n:
        return []
    return [s[i:n + i] for i in range(len(s) - n + 1)]