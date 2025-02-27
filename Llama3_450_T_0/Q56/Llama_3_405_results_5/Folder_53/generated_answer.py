def all_substring_of_size_n(s):
    return list(set((s[i:i + 25] for i in range(len(s) - 24) if len(set(s[i:i + 25])) == 25)))