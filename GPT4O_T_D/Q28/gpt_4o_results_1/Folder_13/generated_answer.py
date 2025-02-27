def return_nth_smallest_ascii(s):
    sub_string = s[47:81]
    ascii_values = sorted((ord(char) for char in sub_string))
    return chr(ascii_values[3]) if len(ascii_values) >= 4 else None