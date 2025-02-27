def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s if 1 <= s.index(char) <= 31]
    ascii_values.sort()
    return chr(ascii_values[5])