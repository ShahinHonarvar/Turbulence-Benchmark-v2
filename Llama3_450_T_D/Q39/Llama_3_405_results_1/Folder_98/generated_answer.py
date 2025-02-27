def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x), reverse=True)
    return ascii_sorted[:68]