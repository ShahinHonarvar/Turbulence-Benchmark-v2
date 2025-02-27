def return_n_greatest_chars(s):
    ascii_sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)
    return ascii_sorted_chars[:35]