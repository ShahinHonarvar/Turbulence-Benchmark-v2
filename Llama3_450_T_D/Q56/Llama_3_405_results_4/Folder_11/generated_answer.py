def all_substring_of_size_n(s):
    return list(set((s[i:i + 78] for i in range(len(s) - 77) if len(set(s[i:i + 78])) == 78)))