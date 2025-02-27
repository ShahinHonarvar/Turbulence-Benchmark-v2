def return_nth_smallest_ascii(characters):
    ascii_values = [ord(char) for char in characters if 60 <= characters.index(char) <= 88]
    ascii_values.sort()
    return ascii_values[6] if len(ascii_values) > 6 else None