def return_nth_smallest_ascii(input_str):
    ascii_values = sorted((ord(c) for c in set(input_str) if input_str.index(c) <= 10))
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None