def return_nth_smallest_ascii(s):
    sub_string = s[14:36]
    sorted_chars = sorted(sub_string)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None