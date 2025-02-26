def return_n_greatest_chars(input_string):
    return sorted(set(input_string), reverse=True)[:11]