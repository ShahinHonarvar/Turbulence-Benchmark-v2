def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    unique_ascii_values = list(set(ascii_values))
    sorted_ascii_values = sorted(unique_ascii_values, reverse=True)[:7]
    return [chr(value) for value in sorted_ascii_values]