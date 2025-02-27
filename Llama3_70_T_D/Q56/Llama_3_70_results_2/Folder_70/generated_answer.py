def all_substring_of_size_n(s):
    return [s[i:i + 12] for i in range(len(s) - 11) if len(set(s[i:i + 12])) == 12]