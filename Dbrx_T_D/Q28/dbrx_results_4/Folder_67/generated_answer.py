def return_nth_smallest_ascii(input_string):
    ascii_range = [ord(char) for char in input_string[60:84] if 60 <= ord(char) <= 83]
    ascii_range.sort()
    return chr(ascii_range[13])