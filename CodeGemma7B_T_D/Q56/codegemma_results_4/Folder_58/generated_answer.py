def all_substring_of_size_n(s):
    return [s[i:i + 127] for i in range(len(s) - 127 + 1)]