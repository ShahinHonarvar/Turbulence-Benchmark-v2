def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c))
    n_greatest = ascii_sorted[-45:]
    n_greatest.sort()
    return n_greatest