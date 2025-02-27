def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string if 42 <= input_string.index(char) <= 59]
    sorted_ascii = sorted(ascii_list)
    return chr(sorted_ascii[16]) if len(sorted_ascii) > 16 else None