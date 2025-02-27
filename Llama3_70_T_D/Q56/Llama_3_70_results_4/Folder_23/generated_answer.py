def all_substring_of_size_n(s):
    return [''.join(set(sub)) for sub in [s[i:i + 42] for i in range(len(s) - 41)] if len(set(sub)) == 42]