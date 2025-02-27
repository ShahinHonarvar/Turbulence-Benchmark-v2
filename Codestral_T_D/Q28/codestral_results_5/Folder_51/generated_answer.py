def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s[10:74]]
    ascii_values.sort()
    return chr(ascii_values[8])