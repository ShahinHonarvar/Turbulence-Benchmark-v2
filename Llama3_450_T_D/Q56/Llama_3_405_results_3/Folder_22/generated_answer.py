def all_substring_of_size_n(s):
    return list(set((s[i:i + 22] for i in range(len(s) - 21) if len(set(s[i:i + 22])) == 22)))