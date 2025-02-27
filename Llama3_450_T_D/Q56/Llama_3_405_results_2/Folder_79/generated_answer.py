def all_substring_of_size_n(s):
    return list(set((s[i:i + 61] for i in range(len(s) - 60) if len(set(s[i:i + 61])) == 61)))