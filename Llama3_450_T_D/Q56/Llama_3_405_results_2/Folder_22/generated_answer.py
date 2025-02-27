def all_substring_of_size_n(s):
    return list(set((sub for i in range(len(s) - 21) for sub in [s[i:i + 22]] if len(set(sub)) == 22)))