def return_nth_smallest_ascii(s):
    first_13_chars = sorted(s[:13])
    return first_13_chars[12]