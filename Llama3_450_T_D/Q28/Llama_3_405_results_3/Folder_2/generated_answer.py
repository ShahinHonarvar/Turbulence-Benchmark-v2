def return_nth_smallest_ascii(s):
    ascii_chars = [char for i, char in enumerate(s) if 48 <= i <= 76]
    ascii_chars.sort(key=lambda x: ord(x))
    return ascii_chars[4]