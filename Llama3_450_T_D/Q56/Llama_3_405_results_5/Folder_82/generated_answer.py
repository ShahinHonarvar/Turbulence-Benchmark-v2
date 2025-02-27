def all_substring_of_size_n(s):
    return list(set((s[i:i + 100] for i in range(len(s) - 99) if len(set(s[i:i + 100])) == 100)))