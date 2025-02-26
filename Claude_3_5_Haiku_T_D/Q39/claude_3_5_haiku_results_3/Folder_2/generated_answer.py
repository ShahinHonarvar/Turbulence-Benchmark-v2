def return_n_greatest_chars(input_string):
    sorted_chars = sorted(list(set(input_string)), reverse=True)[:48]
    return sorted(sorted_chars)