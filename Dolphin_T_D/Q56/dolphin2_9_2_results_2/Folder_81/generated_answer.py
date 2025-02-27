def all_substring_of_size_n(s):
    if len(s) < 98:
        return []
    return list(set((s[i:i + 98] for i in range(len(s) - 97) if len(set(s[i:i + 98])) == 98)))