def return_nth_smallest_ascii(string):
    ascii_values = [ord(string[i]) for i in range(67, 78)]
    ascii_values.sort()
    return chr(ascii_values[7 - 1])