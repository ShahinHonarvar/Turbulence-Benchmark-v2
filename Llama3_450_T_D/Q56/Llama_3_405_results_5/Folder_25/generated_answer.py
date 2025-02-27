def all_substring_of_size_n(s):
    if len(s) < 67:
        return []
    return list(set((s[i:i + 67] for i in range(len(s) - 66) if len(set(s[i:i + 67])) == 67)))