def return_nth_smallest_ascii(s):
    sliced_string = s[52:80]
    unique_chars = set(sliced_string)
    ascii_values = [ord(c) for c in unique_chars]
    ascii_values.sort()
    return chr(ascii_values[6])