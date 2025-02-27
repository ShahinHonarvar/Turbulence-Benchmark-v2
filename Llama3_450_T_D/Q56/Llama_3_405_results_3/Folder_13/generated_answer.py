def all_substring_of_size_n(s):
    return list(set((s[i:i + 53] for i in range(len(s) - 52) if len(set(s[i:i + 53])) == 53)))