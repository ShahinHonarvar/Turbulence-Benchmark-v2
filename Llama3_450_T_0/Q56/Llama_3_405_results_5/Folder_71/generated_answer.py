def all_substring_of_size_n(s):
    return list(set((s[i:i + 17] for i in range(len(s) - 16) if len(set(s[i:i + 17])) == 17)))