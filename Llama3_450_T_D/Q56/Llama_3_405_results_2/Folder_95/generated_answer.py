def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    return list(set((s[i:i + 89] for i in range(len(s) - 88) if len(set(s[i:i + 89])) == 89)))