def return_nth_smallest_ascii(characters):
    ascii_range = [ord(char) for char in characters if 32 <= ord(char) <= 67]
    ascii_range.sort()
    return ascii_range[11] if len(ascii_range) > 12 else None