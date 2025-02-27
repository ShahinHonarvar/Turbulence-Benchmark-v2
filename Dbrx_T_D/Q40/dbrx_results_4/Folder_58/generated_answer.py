def return_n_smallest_chars(input_string):
    input_string = sorted(input_string, key=lambda x: ord(x))
    return input_string[:49][::-1]