def return_n_greatest_chars(input_string):
    sorted_ascii_values = sorted(list(map(ord, input_string)))[:-81:-1]
    n_greatest_chars = [chr(i) for i in sorted_ascii_values]
    return n_greatest_chars