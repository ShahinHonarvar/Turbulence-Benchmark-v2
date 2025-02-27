def return_n_smallest_chars(s):
    result = sorted(s)[:13]
    result.sort(reverse=True)
    return result