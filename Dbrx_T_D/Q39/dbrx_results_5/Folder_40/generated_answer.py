def return_n_greatest_chars(input_string):
    unique_chars = list(set(input_string))
    unique_chars.sort(reverse=True)
    return unique_chars[:7]