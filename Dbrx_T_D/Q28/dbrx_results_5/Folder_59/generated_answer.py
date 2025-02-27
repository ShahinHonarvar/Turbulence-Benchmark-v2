def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s if 0 <= s.index(char) <= 11]
    ascii_values.sort()
    return chr(ascii_values[11])