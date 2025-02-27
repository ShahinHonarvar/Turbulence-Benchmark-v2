def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, reverse=True)
    greatest_chars = sorted_chars[:23]
    return sorted(greatest_chars)