def all_substring_of_size_n(s):
    return list(set((s[i:i + 57] for i in range(len(s) - 56) if len(set(s[i:i + 57])) == 57)))