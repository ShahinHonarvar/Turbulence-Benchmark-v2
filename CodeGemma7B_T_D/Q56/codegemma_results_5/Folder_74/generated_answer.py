def all_substring_of_size_n(s):
    return sorted(set([s[i:i + n] for i in range(len(s) - n + 1) for n in range(98, 0, -1)]))