def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(input_string), key=ord)
    result = sorted_chars[:66][::-1]
    return result