def return_nth_smallest_ascii(s):
    ascii_chars = [char for i, char in enumerate(s) if 32 <= i <= 67]
    unique_chars = sorted(set(ascii_chars), key=lambda x: ord(x))
    return unique_chars[11]