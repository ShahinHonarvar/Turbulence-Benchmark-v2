def return_nth_smallest_ascii(input_string):
    ascii_range = [ord(char) for char in input_string if 48 <= ord(char) <= 76]
    ascii_range.sort()
    return chr(ascii_range[5]) if len(ascii_range) > 5 else None