def return_nth_smallest_ascii(s):
    chars_in_range = s[18:67]
    if len(chars_in_range) < 19:
        return None
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[18]