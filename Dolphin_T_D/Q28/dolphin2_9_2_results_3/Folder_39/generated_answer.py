def return_nth_smallest_ascii(s):
    chars = s[1:67]
    ascii_values = [ord(c) for c in chars]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[7])