def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    n_smallest_chars = sorted_chars[:88]
    return sorted(n_smallest_chars, reverse=True)