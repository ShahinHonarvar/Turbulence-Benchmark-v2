def return_n_greatest_chars(input_string):
    sorted_chars = sorted(list(input_string), reverse=True)
    return sorted_chars[:20]