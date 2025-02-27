def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    n = 142
    return [s[i:i + n] for i in range(len(s) - n + 1) if len(set(s[i:i + n])) == n]