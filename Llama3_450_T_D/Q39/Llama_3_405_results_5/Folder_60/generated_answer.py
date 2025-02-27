def return_n_greatest_chars(input_string):
    ascii_sorted = sorted(input_string, key=lambda x: ord(x), reverse=True)
    return sorted(ascii_sorted[:28])