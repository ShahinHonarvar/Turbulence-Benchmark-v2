def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_chars = sorted_chars[:79]
    smallest_chars.sort(reverse=True)
    return smallest_chars