def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x))
    return ascii_sorted[::-1][:61]