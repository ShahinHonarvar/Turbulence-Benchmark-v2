def return_nth_smallest_ascii(s):
    characters = s[33:61]
    ascii_values = {ord(c): c for c in characters}
    sorted_values = sorted(ascii_values.keys(), key=lambda x: (ascii_values[x], x))
    return ascii_values[sorted_values[17]]