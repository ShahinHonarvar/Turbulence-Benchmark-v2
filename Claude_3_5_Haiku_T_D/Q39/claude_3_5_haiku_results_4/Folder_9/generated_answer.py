def return_n_greatest_chars(input_string):
    sorted_chars = sorted(set(input_string), reverse=True)[:20]
    return sorted(sorted_chars)