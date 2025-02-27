def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)[:76]
    result = sorted(sorted_chars, key=ord, reverse=True)
    return result