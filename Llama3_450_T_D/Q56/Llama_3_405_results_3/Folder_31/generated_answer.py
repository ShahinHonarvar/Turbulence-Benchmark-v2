def all_substring_of_size_n(s):
    return list(set((s[i:i + 46] for i in range(len(s) - 45) if len(set(s[i:i + 46])) == 46)))