def all_substring_of_size_n(s):
    n = len(s)
    subs = [s[i:j] for i in range(n) for j in range(i + 12, n + 1)]
    subs = [i for i in subs if len(i) == len(set(i))]
    return subs