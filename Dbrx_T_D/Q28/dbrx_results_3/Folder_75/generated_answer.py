def return_nth_smallest_ascii(characters):
    ascii_range = [ord(c) for c in characters if 62 <= ord(c) <= 83]
    return chr(sorted(ascii_range)[8])