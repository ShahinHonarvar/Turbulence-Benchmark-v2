def all_substring_of_size_n(s):
    return list(set((s[i:i + 114] for i in range(len(s) - 113) if len(set(s[i:i + 114])) == 114)))