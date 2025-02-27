def return_nth_smallest_ascii(s):
    smallest_ascii_chars = sorted(s[:14], key=lambda x: ord(x))
    return smallest_ascii_chars[13]