def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_chars = sorted_chars[:88]
    smallest_chars.reverse()
    return smallest_chars