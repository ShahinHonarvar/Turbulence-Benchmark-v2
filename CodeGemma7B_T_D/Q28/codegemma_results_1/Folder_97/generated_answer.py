def return_nth_smallest_ascii(str):
    ascii_values = [ord(char) for char in str]
    filtered_values = ascii_values[15:22]
    filtered_values.sort()
    return chr(filtered_values[5])