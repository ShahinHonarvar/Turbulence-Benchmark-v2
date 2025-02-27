def return_n_smallest_chars(str):
    str = sorted(str)
    str = str[:77]
    str.sort(reverse=True)
    return str