def all_substring_of_size_n(s):
    return list(set((sub for i in range(len(s) - 14) for sub in [s[i:i + 15]] if len(set(sub)) == 15)))