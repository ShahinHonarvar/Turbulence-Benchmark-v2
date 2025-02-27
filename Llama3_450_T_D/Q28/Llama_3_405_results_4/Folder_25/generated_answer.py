def return_nth_smallest_ascii(s):
    sliced_string = s[34:69]
    ascii_values = [ord(c) for c in sliced_string]
    unique_values = sorted(set(ascii_values))
    sixth_smallest = unique_values[5]
    return chr(sixth_smallest)