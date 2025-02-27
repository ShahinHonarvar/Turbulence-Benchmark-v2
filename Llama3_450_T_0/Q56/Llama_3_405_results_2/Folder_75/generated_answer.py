def all_substring_of_size_n(s):
    return list(set((s[i:i + 16] for i in range(len(s) - 15) if len(set(s[i:i + 16])) == 16)))