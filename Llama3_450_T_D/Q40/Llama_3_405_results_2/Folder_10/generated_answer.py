def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x))
    smallest_88 = ascii_sorted[:88]
    return sorted(smallest_88, reverse=True)