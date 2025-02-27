def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string[50:77] if char != ' ']
    ascii_values.sort()
    return chr(ascii_values[10])