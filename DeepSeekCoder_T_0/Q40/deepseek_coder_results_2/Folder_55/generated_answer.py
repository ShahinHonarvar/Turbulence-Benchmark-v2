def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_75 = sorted_chars[:75]
    return smallest_75[::-1]