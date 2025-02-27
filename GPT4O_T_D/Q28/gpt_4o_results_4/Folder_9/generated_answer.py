def return_nth_smallest_ascii(s):
    chars_between_indices = sorted(s[10:91])
    if len(chars_between_indices) < 20:
        return None
    return chars_between_indices[19]