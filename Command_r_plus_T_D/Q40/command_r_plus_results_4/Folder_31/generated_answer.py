def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    smallest_70_chars = list(s[:70])
    return smallest_70_chars[::-1]