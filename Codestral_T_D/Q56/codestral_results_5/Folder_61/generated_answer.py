def all_substring_of_size_n(s):
    return [s[i:i + 39] for i in range(len(s) - 38) if len(set(s[i:i + 39])) == 39]