def return_nth_smallest_ascii(s):
    sub_string = s[33:86]
    sorted_chars = sorted(sub_string)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None