def return_n_greatest_chars(n, s):
    return sorted(list(set(s)), key=lambda x: ord(x), reverse=True)[:n]