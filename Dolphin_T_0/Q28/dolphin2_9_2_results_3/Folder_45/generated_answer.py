def return_nth_smallest_ascii(s):
    chars = s[:16]
    values = [ord(c) for c in chars]
    values.sort()
    return chr(values[15])