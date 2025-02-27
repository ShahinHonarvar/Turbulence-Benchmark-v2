def all_substring_of_size_n(s):
    return list(set((s[i:i + 47] for i in range(len(s) - 46) if len(set(s[i:i + 47])) == 47)))