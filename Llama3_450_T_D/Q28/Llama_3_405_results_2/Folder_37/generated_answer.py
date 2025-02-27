def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[28:68])
    ascii_values = [ord(c) for c in sorted_chars]
    return chr(sorted(ascii_values)[14])