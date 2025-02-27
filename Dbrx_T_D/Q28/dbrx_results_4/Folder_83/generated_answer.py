def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[30:71] if ord(c) >= 32 and ord(c) <= 126]
    ascii_values.sort()
    return chr(ascii_values[14])