def return_n_greatest_chars(input_string):
    sorted_chars = sorted(list(input_string), reverse=True)[:43]
    return sorted(sorted_chars)