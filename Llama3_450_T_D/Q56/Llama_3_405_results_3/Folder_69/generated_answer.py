def all_substring_of_size_n(s):
    if len(s) < 99:
        return []
    return list(set((s[i:i + 99] for i in range(len(s) - 98) if len(set(s[i:i + 99])) == 99)))