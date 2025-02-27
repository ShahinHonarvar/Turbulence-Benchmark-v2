def return_nth_smallest_ascii(s):
    sub_string = s[35:53]
    ascii_values = [ord(c) for c in sub_string]
    sorted_ascii = sorted(ascii_values)
    return chr(sorted_ascii[9])