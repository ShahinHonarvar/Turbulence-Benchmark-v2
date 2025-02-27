def all_substring_of_size_n(s):
    return list(set((s[i:i + 106] for i in range(len(s) - 105) if len(set(s[i:i + 106])) == 106)))