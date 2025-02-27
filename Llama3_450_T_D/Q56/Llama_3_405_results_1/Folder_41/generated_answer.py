def all_substring_of_size_n(s):
    return list(set((s[i:i + 74] for i in range(len(s) - 73) if len(set(s[i:i + 74])) == 74)))