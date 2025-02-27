def all_substring_of_size_n(s):
    substrings = set((s[i:i + 14] for i in range(len(s) - 13) if len(set(s[i:i + 14])) == 14))
    return list(substrings)