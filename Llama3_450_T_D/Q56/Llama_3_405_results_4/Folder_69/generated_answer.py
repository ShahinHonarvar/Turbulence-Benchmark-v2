def all_substring_of_size_n(s):
    return list(set((s[i:i + 99] for i in range(len(s) - 98) if len(set(s[i:i + 99])) == 99)))