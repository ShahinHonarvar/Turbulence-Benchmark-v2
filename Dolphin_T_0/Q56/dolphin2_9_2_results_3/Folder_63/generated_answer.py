def all_substring_of_size_n(s):
    return [s[i:i + 19] for i in range(len(s) - 19) if len(set(s[i:i + 19])) == 19]