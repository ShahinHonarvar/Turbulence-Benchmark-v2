def return_nth_smallest_ascii(s):
    if len(s) < 17:
        return None
    sub_string = s[:17]
    sorted_chars = sorted(sub_string)
    return sorted_chars[16]