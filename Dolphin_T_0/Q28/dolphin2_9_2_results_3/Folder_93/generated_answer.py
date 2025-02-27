def return_nth_smallest_ascii(string):
    ascii_values = [ord(string[i]) for i in range(42, 60)]
    ascii_values.sort()
    return chr(ascii_values[16])