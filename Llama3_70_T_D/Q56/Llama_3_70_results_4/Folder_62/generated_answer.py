def all_substring_of_size_n(s):
    return [s[i:i + 32] for i in range(len(s) - 31) if len(set(s[i:i + 32])) == 32]