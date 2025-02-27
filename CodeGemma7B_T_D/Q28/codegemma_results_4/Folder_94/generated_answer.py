def return_nth_smallest_ascii(some_str):
    filtered_str = some_str[6:59 + 1]
    ascii_values = [ord(char) for char in filtered_str]
    ascii_values.sort()
    return chr(ascii_values[18])