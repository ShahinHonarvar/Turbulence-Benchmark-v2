def all_substring_of_size_n(s):
    return [s[i:i + 106] for i in range(len(s) - 106 + 1) if len(set(s[i:i + 106])) == 106]