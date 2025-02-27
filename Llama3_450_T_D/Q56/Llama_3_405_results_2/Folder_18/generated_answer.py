def all_substring_of_size_n(s):
    return list(set((s[i:i + 63] for i in range(len(s) - 62) if len(set(s[i:i + 63])) == 63)))