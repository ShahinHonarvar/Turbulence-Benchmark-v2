def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:38]
    smallest_chars.sort(reverse=True)
    return smallest_chars