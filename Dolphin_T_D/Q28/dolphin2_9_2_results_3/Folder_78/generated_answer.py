def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[0:88]]
    ascii_values.sort()
    return chr(ascii_values[13])