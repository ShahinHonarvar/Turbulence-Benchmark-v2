def all_substring_of_size_n(s):
    n = 3
    return [''.join(filter(lambda x: x not in a[:i], a[:i + n] if i < len(a) - n else a[i:a.index(' ')])) for i in range(len(s) - n + 1) if len(set(a[i:i + n])) == n]