def return_nth_smallest_ascii(str):
    ascii_values = [ord(char) for char in str]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[10])