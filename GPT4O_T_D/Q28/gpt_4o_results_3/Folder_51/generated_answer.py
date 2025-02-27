def return_nth_smallest_ascii(s):
    if len(s) < 74:
        return None
    sub_string = s[10:74]
    sorted_chars = sorted(sub_string)
    return sorted_chars[8]