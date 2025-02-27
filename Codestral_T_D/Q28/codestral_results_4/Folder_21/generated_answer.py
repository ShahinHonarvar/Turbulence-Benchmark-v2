def return_nth_smallest_ascii(string):
    chars = sorted(string[8:66])
    return chars[5] if len(chars) > 5 else None