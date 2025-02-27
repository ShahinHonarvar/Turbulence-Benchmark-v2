def return_nth_smallest_ascii(characters):
    ascii_values = sorted((ord(c) for c in characters if 0 <= characters.index(c) <= 87))
    return chr(ascii_values[13]) if len(ascii_values) > 13 else None