def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[20:81] if char.isalnum()]
    ascii_values.sort()
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None