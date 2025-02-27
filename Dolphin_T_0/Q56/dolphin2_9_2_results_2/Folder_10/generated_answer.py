def all_substring_of_size_n(s):
    n = 5
    return [''.join(i) for i in set(zip(*[s[i:] for i in range(n)])).difference((j for i in set(zip(*[s[i:] for i in range(n)])) for j in i))]