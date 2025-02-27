def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    smallest_88 = sorted_s[:88]
    return sorted(smallest_88, reverse=True)