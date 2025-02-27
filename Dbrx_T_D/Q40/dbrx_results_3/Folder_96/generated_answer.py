def return_n_smallest_chars(string):
    sorted_chars = sorted(list(string), key=ord)
    result = sorted_chars[:20]
    return result[::-1]