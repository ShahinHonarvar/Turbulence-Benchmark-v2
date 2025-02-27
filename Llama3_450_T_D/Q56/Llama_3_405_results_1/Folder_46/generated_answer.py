def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    return list(set((s[i:i + 87] for i in range(len(s) - 86) if len(set(s[i:i + 87])) == 87)))