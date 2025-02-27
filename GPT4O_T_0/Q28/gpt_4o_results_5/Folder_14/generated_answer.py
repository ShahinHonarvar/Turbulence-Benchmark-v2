def return_nth_smallest_ascii(s):
    sub_string = s[46:83]
    sorted_chars = sorted(sub_string)
    return sorted_chars[15] if len(sorted_chars) >= 16 else None