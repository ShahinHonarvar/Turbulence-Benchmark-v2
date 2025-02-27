def return_n_greatest_chars(input_string):
    if len(input_string) > 10:
        sorted_chars = sorted(input_string, reverse=True)[:11]
    else:
        sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars