def all_substring_of_size_n(s):
    return [s[i:i + 86] for i in range(len(s) - 85) if len(set(s[i:i + 86])) == 86]