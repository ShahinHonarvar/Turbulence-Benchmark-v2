def return_n_greatest_chars(input_string):
    input_string = list(set(input_string))
    input_string.sort(key=lambda x: ord(x), reverse=True)
    return input_string[:32]