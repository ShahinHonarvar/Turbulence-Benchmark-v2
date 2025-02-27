def return_nth_smallest_ascii(s):
    chars_in_range = sorted((c for c in s if 58 <= ord(c) <= 85))
    if len(chars_in_range) < 19:
        return None
    return chars_in_range[18]