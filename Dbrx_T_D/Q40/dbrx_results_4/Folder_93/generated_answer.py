def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string), key=ord)
    return sorted_chars[-77:][::-1]