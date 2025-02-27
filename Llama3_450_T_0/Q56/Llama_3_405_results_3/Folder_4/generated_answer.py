def all_substring_of_size_n(s):
    return list(set((s[i:i + 41] for i in range(len(s) - 40) if len(set(s[i:i + 41])) == 41)))