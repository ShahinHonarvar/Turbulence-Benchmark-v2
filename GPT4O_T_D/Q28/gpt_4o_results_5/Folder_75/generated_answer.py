def return_nth_smallest_ascii(s):
    sub_string = s[62:84]
    ascii_values = sorted(sub_string, key=lambda x: ord(x))
    return ascii_values[8] if len(ascii_values) >= 9 else None