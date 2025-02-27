def return_n_smallest_chars(s):
    result = sorted(s)[:36]
    return sorted(result, reverse=True)