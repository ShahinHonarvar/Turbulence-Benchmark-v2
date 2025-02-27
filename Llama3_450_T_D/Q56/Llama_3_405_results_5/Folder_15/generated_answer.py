def all_substring_of_size_n(s):
    return list(set((s[i:i + 3] for i in range(len(s) - 2) if len(set(s[i:i + 3])) == 3)))