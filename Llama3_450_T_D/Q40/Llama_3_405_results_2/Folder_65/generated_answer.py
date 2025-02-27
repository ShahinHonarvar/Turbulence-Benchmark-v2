def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    smallest_chars = unique_chars[:27]
    smallest_chars.sort(reverse=True)
    return smallest_chars