def return_nth_smallest_ascii(s):
    ascii_values = sorted(list(set(s[0:15])))
    if len(ascii_values) >= 15:
        return chr(ascii_values[14])
    else:
        return None