def return_n_smallest_chars(str):
    list = sorted(str, key=ord, reverse=True)
    return list[:75]