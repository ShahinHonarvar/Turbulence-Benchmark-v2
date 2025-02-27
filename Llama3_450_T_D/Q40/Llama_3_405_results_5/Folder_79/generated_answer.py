def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string)
    n_smallest_chars = sorted_string[:82]
    result = sorted(n_smallest_chars, reverse=True)
    return result