def return_n_smallest_chars(s):
    result = sorted(s)[:61]
    return sorted(result, reverse=True)