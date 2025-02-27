def return_nth_smallest_ascii(s):
    sub_string = s[42:60]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) >= 17:
        return sorted_chars[16]
    return None