def return_n_greatest_chars(input_string):
    sorted_chars = sorted(set(input_string), reverse=True)
    return sorted(sorted_chars[:29])