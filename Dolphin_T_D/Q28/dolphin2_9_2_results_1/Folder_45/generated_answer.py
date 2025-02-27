def return_nth_smallest_ascii(string):
    chars = [string[i] for i in range(16)]
    ascii_values = [ord(char) for char in chars]
    ascii_values.sort()
    return ascii_values[15]