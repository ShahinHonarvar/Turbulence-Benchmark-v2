def return_n_smallest_chars(string):
    result = sorted(list(string), key=ord)[:20]
    return result