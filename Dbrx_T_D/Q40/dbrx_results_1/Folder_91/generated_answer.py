def return_n_smallest_chars(input_string):
    input_string = sorted(input_string, key=lambda x: ord(x))
    if len(input_string) > 6:
        input_string = input_string[:6]
    return input_string[::-1]