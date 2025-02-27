def return_nth_smallest_ascii(s):
    ascii_values = sorted(s[:5])
    return ascii_values[3] if len(ascii_values) >= 4 else None