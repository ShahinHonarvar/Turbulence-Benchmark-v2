def all_substring_of_size_n(s):
    return list(set([s[i:i + 77] for i in range(len(s) - 76) if len(set(s[i:i + 77])) == 77]))