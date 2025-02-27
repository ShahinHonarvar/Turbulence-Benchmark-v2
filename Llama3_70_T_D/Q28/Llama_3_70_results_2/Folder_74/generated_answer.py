def return_nth_smallest_ascii(s):
    ascii_values = [ord(s[i]) for i in range(1, 32) if 1 <= i <= 31]
    ascii_values.sort()
    return chr(ascii_values[5])