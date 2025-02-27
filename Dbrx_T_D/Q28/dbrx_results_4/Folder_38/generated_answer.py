def return_nth_smallest_ascii(char_string):
    ascii_chars = [ord(c) for c in char_string if char_string.index(c) <= 45]
    sorted_ascii = sorted(ascii_chars)[:10]
    return chr(sorted_ascii[9])