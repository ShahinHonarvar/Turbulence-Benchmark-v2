def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if i <= 10])
    return sorted(ascii_chars, key=lambda char: ord(char))[10]