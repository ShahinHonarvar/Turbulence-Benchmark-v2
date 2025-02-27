def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 60 <= input_string.index(char) <= 88]
    return chr(sorted(ascii_values)[6]) if ascii_values else None