def return_nth_smallest_ascii(s):
    if len(s) < 6:
        return None
    else:
        ascii_values = [ord(c) for c in s[:6]]
        ascii_values.sort()
        return chr(ascii_values[5])