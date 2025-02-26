def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string), key=ord)
    result = sorted_chars[:68]
    return sorted(result, reverse=True)