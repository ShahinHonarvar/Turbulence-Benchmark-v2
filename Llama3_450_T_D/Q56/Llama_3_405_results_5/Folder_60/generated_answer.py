def all_substring_of_size_n(s):
    return list(set((s[i:i + 36] for i in range(len(s) - 35) if len(set(s[i:i + 36])) == 36)))