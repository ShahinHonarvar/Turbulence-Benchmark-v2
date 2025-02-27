def all_substring_of_size_n(s):
    n = 29
    return list(set((sub for i in range(len(s) - n + 1) for sub in [s[i:i + n]] if len(set(sub)) == n)))