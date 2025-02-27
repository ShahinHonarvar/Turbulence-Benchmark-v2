def return_n_smallest_chars(str):
    str = sorted(str, key=ord)
    str = str[:75]
    str.sort(reverse=True)
    return str