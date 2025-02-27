def return_n_smallest_chars(s):
    result = sorted(s)[:28]
    return sorted(result, reverse=True)