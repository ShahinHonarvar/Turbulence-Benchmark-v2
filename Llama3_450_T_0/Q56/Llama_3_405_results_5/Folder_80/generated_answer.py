def all_substring_of_size_n(s):
    return list(set((s[i:i + 31] for i in range(len(s) - 30) if len(set(s[i:i + 31])) == 31)))