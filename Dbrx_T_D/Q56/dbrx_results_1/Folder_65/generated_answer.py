def all_substring_of_size_n(s):
    n = 81
    if len(s) < n or len(set(s)) < n:
        return []
    else:
        return [s[i:n + i] for i in range(len(s) - n + 1) if len(set(s[i:n + i])) == n]