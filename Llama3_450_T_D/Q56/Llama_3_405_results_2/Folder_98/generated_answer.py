def all_substring_of_size_n(s):
    return list(set((sub for i in range(len(s) - 9) for sub in [s[i:i + 10]] if len(set(sub)) == 10)))