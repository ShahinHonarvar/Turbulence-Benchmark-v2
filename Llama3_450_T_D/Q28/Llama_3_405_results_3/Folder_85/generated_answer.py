def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 17 <= i <= 86])
    ascii_chars.sort(key=lambda x: ord(x))
    return ascii_chars[14]