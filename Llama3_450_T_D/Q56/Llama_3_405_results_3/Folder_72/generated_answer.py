def all_substring_of_size_n(s):
    return list(set((sub for i in range(len(s) - 87) for sub in [s[i:i + 88]] if len(set(sub)) == 88)))