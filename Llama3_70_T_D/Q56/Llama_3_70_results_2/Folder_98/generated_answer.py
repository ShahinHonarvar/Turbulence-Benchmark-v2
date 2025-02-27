def all_substring_of_size_n(s):
    substrings = set((s[i:i + 10] for i in range(len(s) - 9) if len(set(s[i:i + 10])) == 10))
    return list(substrings)