def all_substring_of_size_n(s):
    return list(set((s[i:i + 48] for i in range(len(s) - 47) if len(set(s[i:i + 48])) == 48)))