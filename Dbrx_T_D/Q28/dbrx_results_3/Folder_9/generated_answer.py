def return_nth_smallest_ascii(s):
    chars = sorted(s)[10:91]
    if len(chars) < 20:
        return None
    return chars[19]