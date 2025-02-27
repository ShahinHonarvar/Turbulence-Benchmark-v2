def return_n_smallest_chars(s):
    sorted_s = sorted(list(s))
    smallest_chars = sorted_s[:72]
    smallest_chars.reverse()
    return smallest_chars