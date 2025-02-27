def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort()
    selected_ascii_values = ascii_values[:88]
    selected_ascii_values.sort(reverse=True)
    return [chr(ascii_value) for ascii_value in selected_ascii_values]