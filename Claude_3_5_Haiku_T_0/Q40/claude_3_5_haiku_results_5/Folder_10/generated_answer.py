def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:88]
    return sorted(sorted_chars, reverse=True)