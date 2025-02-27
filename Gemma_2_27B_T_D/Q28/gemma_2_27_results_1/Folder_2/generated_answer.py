def return_nth_smallest_ascii(text):
    substring = text[48:77]
    ascii_values = [ord(char) for char in substring]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[4])