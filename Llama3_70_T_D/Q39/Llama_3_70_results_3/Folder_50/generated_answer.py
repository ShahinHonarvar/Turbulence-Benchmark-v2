def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (x not in s[:16], x), reverse=True)[:16]