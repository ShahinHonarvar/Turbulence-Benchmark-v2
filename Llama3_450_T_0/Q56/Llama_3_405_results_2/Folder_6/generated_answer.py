def all_substring_of_size_n(s):
    return list(set((s[i:i + 23] for i in range(len(s) - 22) if len(set(s[i:i + 23])) == 23)))