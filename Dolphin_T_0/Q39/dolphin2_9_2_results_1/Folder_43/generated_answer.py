def return_n_greatest_chars(input_string):
    input_string_sorted = sorted(input_string)
    return input_string_sorted[-56:][::-1]