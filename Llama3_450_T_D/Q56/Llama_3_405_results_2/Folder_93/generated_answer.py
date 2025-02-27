def all_substring_of_size_n(s):
    return list(set((s[i:i + 54] for i in range(len(s) - 53) if len(set(s[i:i + 54])) == 54)))