def return_nth_smallest_ascii(chars):
    ascii_values = [ord(c) for c in chars[4:34]]
    ascii_values.sort()
    return chr(ascii_values[3])