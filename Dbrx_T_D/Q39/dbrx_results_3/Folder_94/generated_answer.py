def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    unique_ascii_values = list(set(ascii_values))
    unique_ascii_values.sort(reverse=True)
    if len(unique_ascii_values) < 87:
        return ''.join([chr(val) for val in unique_ascii_values])
    else:
        return ''.join([chr(val) for val in unique_ascii_values[:87]])