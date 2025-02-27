def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted(ascii_sorted[:40])