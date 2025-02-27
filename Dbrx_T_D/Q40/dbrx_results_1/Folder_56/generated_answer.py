def return_n_smallest_chars(input_string):
    input_string = sorted(list(set(input_string)))
    return input_string[:21]