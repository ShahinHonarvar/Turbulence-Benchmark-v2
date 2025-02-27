def all_substring_of_size_n(s):
    return list(set((sub for i in range(len(s) - 16) for sub in [s[i:i + 17]] if len(set(sub)) == 17)))