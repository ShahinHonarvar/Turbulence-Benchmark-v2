def all_substring_of_size_n(s):
    return list(set((s[i:i + 24] for i in range(len(s) - 23) if len(set(s[i:i + 24])) == 24)))