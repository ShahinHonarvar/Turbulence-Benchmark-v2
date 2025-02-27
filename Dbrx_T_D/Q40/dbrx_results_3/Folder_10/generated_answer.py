def return_n_smallest_chars(input_string):
    input_string = sorted(input_string, key=lambda char: ord(char))
    return input_string[:88]