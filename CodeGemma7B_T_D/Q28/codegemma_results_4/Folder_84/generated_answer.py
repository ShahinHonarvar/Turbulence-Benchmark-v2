def return_nth_smallest_ascii(some_string):
    ascii_values = [ord(char) for char in some_string[52:80] if char.isalpha()]
    ascii_values.sort()
    return chr(ascii_values[6])