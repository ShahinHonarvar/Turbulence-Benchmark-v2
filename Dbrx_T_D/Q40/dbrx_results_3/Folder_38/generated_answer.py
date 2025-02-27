def return_n_smallest_chars(input_string):
    input_string = sorted(set(input_string))
    return input_string[:45]