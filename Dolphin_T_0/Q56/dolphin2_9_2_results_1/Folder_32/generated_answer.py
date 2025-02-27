def all_substring_of_size_n(s):
    n = 71
    ss = [s[i:i + n] for i in range(len(s) - n + 1)]
    return [i for i in ss if set(i) == n]