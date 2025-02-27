def return_nth_smallest_ascii(input_string):
    ascii_range = [ord(char) for char in input_string if 62 <= ord(char) <= 83]
    ascii_range.sort()
    return chr(ascii_range[8]) if len(ascii_range) >= 9 else None