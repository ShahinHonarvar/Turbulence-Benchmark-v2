def return_n_smallest_chars(s):
    sorted_chars = sorted([c for c in s])
    return sorted_chars[:49][::-1]