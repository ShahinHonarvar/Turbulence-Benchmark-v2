def return_nth_smallest_ascii(string):
    valid_chars = sorted(string[10:74])
    if len(valid_chars) < 9:
        return None
    return valid_chars[8]