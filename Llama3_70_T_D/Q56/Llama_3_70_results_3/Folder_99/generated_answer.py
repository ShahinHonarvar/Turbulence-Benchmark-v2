def all_substring_of_size_n(s):
    return [s[i:i + 110] for i in range(len(s) - 109) if len(set(s[i:i + 110])) == 110]