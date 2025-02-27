def all_substring_of_size_n(s):
    size = 69
    return [s[i:i + size] for i in range(len(s) - size + 1) if len(set(s[i:i + size])) == size]