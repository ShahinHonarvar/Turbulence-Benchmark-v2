def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort()
    n_smallest_chars = [chr(value) for value in ascii_values[:6]]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars