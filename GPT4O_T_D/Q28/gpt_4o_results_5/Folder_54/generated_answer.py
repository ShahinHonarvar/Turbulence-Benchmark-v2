def return_nth_smallest_ascii(s):
    sub_string = s[12:88]
    sorted_chars = sorted(sub_string)
    return sorted_chars[16] if len(sorted_chars) >= 17 else None