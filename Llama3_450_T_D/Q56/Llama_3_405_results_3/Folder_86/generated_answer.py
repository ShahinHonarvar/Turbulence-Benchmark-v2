def all_substring_of_size_n(s):
    n = 143
    return list(set((s[i:i + n] for i in range(len(s) - n + 1) if len(set(s[i:i + n])) == n)))