def return_nth_smallest_ascii(input_string):
    ascii_chars = [ord(char) for char in input_string if 47 <= ord(char) <= 80]
    ascii_chars.sort()
    return chr(ascii_chars[3])