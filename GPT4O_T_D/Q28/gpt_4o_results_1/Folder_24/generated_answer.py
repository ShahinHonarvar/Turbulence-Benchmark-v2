def return_nth_smallest_ascii(s):
    sub_string = s[34:82]
    sorted_chars = sorted(sub_string, key=ord)
    return sorted_chars[11] if len(sorted_chars) > 11 else None