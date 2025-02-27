def return_nth_smallest_ascii(s):
    chars = s[:5]
    ascii_values = {ord(c): c for c in chars}
    sorted_ascii = sorted(ascii_values.keys())
    return ascii_values[sorted_ascii[4]]