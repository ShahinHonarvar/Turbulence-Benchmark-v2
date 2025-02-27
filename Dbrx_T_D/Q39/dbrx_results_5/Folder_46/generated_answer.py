def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    filtered_values = [value for value in ascii_values if value >= 54]
    sorted_values = sorted(filtered_values, reverse=True)
    n_greatest_chars = [chr(value) for value in sorted_values[:54]]
    return n_greatest_chars