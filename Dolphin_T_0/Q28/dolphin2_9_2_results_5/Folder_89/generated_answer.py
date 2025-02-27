def return_nth_smallest_ascii(string):
    nth_smallest_ascii_chars = sorted(string[24:72], key=lambda x: ord(x))
    if len(nth_smallest_ascii_chars) >= 8:
        return nth_smallest_ascii_chars[7]