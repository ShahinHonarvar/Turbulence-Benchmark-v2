def return_n_smallest_chars(input_string):
    ascii_values = [ord(c) for c in input_string]
    smallest_chars = sorted(input_string, key=lambda c: ascii_values[input_string.index(c)])
    return sorted(smallest_chars[:47], reverse=True)