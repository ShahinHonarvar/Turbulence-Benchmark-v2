def return_nth_smallest_ascii(s):
    substring = s[47:81]
    ascii_values = sorted([ord(char) for char in substring])
    return chr(ascii_values[3])