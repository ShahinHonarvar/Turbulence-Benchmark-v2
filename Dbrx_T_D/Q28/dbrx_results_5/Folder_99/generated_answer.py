def return_nth_smallest_ascii(s):
    chars = s[17:66]
    ascii_values = [ord(c) for c in chars]
    unique_ascii_values = list(set(ascii_values))
    sorted_ascii_values = sorted(unique_ascii_values)
    return chr(sorted_ascii_values[7]) if len(sorted_ascii_values) > 7 else None