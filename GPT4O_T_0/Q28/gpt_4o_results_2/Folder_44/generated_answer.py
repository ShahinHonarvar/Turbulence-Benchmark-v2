def return_nth_smallest_ascii(s):
    sub_string = s[20:31]
    sorted_chars = sorted(sub_string)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None