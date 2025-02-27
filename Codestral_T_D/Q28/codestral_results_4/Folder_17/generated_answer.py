def return_nth_smallest_ascii(s):
    sliced_chars = sorted(s[4:34])
    if len(sliced_chars) >= 4:
        return sliced_chars[3]
    return None