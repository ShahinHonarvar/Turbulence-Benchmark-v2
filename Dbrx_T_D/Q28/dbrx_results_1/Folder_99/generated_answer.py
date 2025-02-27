def return_nth_smallest_ascii(characters):
    ascii_values = sorted((ord(c) for c in characters if 17 <= characters.index(c) <= 65))
    if len(ascii_values) >= 8:
        return chr(ascii_values[7])
    else:
        return None