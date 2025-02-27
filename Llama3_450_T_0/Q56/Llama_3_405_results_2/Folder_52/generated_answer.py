def all_substring_of_size_n(s):
    return list(set((s[i:i + 15] for i in range(len(s) - 14) if len(set(s[i:i + 15])) == 15)))