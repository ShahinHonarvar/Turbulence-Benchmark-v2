def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for idx, char in enumerate(s) if 0 <= idx <= 3])
    return sorted(ascii_chars, key=lambda x: ord(x))[3]