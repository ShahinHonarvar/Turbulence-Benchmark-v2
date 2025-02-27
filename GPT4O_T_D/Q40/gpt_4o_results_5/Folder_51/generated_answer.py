def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_45_chars = sorted_chars[:45]
    smallest_45_chars.sort(reverse=True)
    return smallest_45_chars