def return_n_smallest_chars(s):
    smallest_chars = sorted(s)[:2]
    smallest_chars.sort(reverse=True)
    return smallest_chars