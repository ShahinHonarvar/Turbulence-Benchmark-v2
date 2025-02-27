def return_n_greatest_chars(input_string):
    return sorted(list(input_string), key=lambda x: ord(x), reverse=True)[:24]