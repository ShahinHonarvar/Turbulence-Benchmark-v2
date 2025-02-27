def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 33 <= i <= 60], key=lambda x: ord(x))
    return ascii_chars[17]