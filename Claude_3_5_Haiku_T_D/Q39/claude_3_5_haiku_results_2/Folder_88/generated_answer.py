def return_n_greatest_chars(input_string):
    sorted_chars = sorted(set(input_string), reverse=True)[:84]
    return sorted(sorted_chars)