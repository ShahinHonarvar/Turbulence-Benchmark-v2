def return_nth_smallest_ascii(input_string):
    sub_string = input_string[50:76]
    ascii_values = [ord(char) for char in sub_string]
    ascii_values.sort()
    return chr(ascii_values[6])