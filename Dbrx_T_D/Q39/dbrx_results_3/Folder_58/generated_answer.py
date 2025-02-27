def return_n_greatest_chars(input_string):
    if len(input_string) < 49:
        return sorted(input_string, reverse=True)
    else:
        sorted_chars = sorted(input_string, reverse=True)
        return sorted_chars[:49]