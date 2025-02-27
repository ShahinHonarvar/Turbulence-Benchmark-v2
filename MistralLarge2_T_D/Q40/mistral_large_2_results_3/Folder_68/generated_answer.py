def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_89_chars = sorted_chars[:89]
    return sorted(smallest_89_chars, reverse=True)