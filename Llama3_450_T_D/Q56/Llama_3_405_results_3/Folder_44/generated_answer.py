def all_substring_of_size_n(s):
    return list(set((s[i:i + 90] for i in range(len(s) - 89) if len(set(s[i:i + 90])) == 90)))