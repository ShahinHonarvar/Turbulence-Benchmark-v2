def return_nth_smallest_ascii(s):
    chars = s[47:71]
    ascii_values = [ord(char) for char in chars if char.isalpha()]
    ascii_values.sort()
    return chr(ascii_values[13])