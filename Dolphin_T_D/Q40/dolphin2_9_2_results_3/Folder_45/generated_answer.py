def return_n_smallest_chars(input_string):
    ascii_sorted_string = sorted(input_string, key=lambda c: ord(c))
    return ascii_sorted_string[:52]