def return_nth_smallest_ascii(string):
    chars = sorted(string[51:79])
    return chars[8] if len(chars) > 8 else None