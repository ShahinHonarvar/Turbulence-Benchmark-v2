def return_n_smallest_chars(input_string):
    input_string = ''.join(sorted(set(input_string)))
    return input_string[:43]