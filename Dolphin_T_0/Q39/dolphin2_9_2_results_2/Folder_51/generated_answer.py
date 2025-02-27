def return_n_greatest_chars(input_string):
    input_string = list(input_string)
    input_string.sort(reverse=True)
    return input_string[:45]