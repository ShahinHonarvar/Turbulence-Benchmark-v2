def return_nth_smallest_ascii(s):
    if len(s) < 16:
        return None
    sub_string = s[:16]
    sorted_chars = sorted(sub_string)
    return sorted_chars[15]