def return_n_smallest_chars(s):
    return sorted(''.join(sorted(s)[:63]))