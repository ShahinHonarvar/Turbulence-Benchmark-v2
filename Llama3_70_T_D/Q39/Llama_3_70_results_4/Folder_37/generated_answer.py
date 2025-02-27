def return_n_greatest_chars(s, n=26):
    return sorted(s, key=lambda c: ord(c), reverse=True)[:n]