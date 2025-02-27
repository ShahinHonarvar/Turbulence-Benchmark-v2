def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[44:70]]
    sorted_ascii = sorted(ascii_values)
    return chr(sorted_ascii[14])