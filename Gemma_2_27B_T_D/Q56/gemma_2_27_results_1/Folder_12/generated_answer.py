def all_substring_of_size_n(s):
    return [t for i in range(len(s) - 46) for t in [s[i:i + 47]] if len(set(t)) == 47]