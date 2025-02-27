def return_n_smallest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_ascii_values = sorted(ascii_values)[:88]
    chars = [chr(value) for value in sorted_ascii_values]
    return chars[::-1]