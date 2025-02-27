def return_n_smallest_chars(s):
    result = sorted(s)[:89]
    return sorted(result, reverse=True)