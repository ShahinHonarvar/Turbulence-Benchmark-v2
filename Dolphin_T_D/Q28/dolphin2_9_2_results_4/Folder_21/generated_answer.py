def return_nth_smallest_ascii(s):
    substring = s[8:65]
    ascii_values = [ord(c) for c in substring]
    sorted_values = sorted(ascii_values)
    return list(substring)[ascii_values.index(sorted_values[5])]