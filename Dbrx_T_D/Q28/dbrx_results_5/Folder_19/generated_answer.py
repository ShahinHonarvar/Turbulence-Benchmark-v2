def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in set(input_string) if input_string.index(char) in range(19)]
    ascii_values.sort()
    return chr(ascii_values[12])