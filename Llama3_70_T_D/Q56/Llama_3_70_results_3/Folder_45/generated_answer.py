def all_substring_of_size_n(s):
    substrings = set((s[i:i + 29] for i in range(len(s) - 28) if len(set(s[i:i + 29])) == 29))
    return list(substrings)