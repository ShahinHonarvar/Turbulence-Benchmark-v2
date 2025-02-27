def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, reverse=True)[:68]
    return sorted(sorted_chars)