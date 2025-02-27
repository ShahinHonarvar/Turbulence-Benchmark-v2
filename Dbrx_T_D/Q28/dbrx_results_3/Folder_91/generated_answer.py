def return_nth_smallest_ascii(chars):
    chars_in_range = [c for c in chars if 0 <= chars.index(c) <= 7]
    chars_in_range.sort(key=lambda char: ord(char))
    return chars_in_range[7]