def return_nth_smallest_ascii(s):
    sub_str = s[15:22]
    ascii_values = [ord(char) for char in sub_str]
    ascii_values.sort()
    sixth_smallest = ascii_values[5]
    sixth_smallest_char = chr(sixth_smallest)
    return sixth_smallest_char