def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(char) for char in input_string if ord(char) in range(ord('!'), ord('-') + 1)))
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None