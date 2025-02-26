def return_n_greatest_chars(input_string):
    sorted_chars = sorted(set(input_string), reverse=True)[:19]
    return sorted(sorted_chars)