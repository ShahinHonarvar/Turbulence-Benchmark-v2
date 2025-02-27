def return_nth_smallest_ascii(chars):
    ordered_chars = sorted(chars[34:82], key=ord)
    return ordered_chars[11]