def all_substring_of_size_n(s):
    return list(set((s[i:i + 127] for i in range(len(s) - 126) if len(set(s[i:i + 127])) == 127)))