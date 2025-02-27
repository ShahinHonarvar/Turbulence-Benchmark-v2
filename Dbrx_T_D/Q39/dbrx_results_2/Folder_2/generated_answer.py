def return_n_greatest_chars(input_string):
    input_string = [char for char in set(input_string)]
    input_string.sort(key=lambda x: ord(x))
    return input_string[-48:]