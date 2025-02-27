def return_n_smallest_chars(input_string):
    input_string = sorted(input_string, key=ord)
    return input_string[:7][::-1]