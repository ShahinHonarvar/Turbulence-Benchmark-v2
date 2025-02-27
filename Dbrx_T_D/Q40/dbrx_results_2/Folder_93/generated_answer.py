def return_n_smallest_chars(input_string):
    ascii_values = sorted(list(set((ord(char) for char in input_string))))[:77]
    return sorted(ascii_values, reverse=True)