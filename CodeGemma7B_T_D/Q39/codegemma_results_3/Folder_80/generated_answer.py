def return_n_greatest_chars(input_string):
    return sorted(input_string, key=lambda k: ord(k), reverse=True)[:35]