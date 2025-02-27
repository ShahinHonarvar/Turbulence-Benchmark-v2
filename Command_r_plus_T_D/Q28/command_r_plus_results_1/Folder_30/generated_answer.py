def return_nth_smallest_ascii(s):
    ascii_values = [ord(s[i]) for i in range(50, 77)]
    ascii_values.sort()
    return chr(ascii_values[10])