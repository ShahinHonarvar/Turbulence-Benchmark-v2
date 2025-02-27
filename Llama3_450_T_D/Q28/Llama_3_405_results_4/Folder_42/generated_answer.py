def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 12 <= i <= 72])
    return sorted(ascii_chars, key=lambda x: ord(x))[12]