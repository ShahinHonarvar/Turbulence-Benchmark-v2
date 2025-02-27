def all_substring_of_size_n(s):
    return list(set((s[i:i + 79] for i in range(len(s) - 78) if len(set(s[i:i + 79])) == 79)))