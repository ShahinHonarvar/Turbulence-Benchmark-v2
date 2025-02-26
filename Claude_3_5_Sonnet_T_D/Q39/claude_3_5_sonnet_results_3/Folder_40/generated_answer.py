def return_n_greatest_chars(input_string):
    return sorted(list(set(input_string)), reverse=True)[:7]