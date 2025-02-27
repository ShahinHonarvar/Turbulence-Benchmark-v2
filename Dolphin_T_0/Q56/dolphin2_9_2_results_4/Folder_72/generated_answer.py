def all_substring_of_size_n(s):
    n = 88
    return [''.join(i) for i in set([s[j:j + n] for j in range(len(s) - n + 1) if len(set(s[j:j + n])) == n])]