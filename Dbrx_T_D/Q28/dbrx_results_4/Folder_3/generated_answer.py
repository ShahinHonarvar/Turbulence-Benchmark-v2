def return_nth_smallest_ascii(chars):
    ascii_values = [ord(char) for char in chars[25:46] if char.islower()]
    ascii_values.sort()
    return chr(ascii_values[10])