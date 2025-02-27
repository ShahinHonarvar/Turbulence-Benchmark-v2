def return_nth_smallest_ascii(s):
    if len(s) < 70:
        limited_string = s
    else:
        limited_string = s[:70]
    sorted_chars = sorted(limited_string)
    return sorted_chars[9] if len(sorted_chars) > 9 else None