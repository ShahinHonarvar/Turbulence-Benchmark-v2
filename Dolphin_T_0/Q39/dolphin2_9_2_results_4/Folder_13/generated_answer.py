def return_n_greatest_chars(input_string):
    return sorted([x for x in input_string], reverse=True)[:31]