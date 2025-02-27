def all_substring_of_size_n(s):
    substrings = set((s[i:i + 77] for i in range(len(s)) if len(set(s[i:i + 77])) == 77))
    return list(substrings)