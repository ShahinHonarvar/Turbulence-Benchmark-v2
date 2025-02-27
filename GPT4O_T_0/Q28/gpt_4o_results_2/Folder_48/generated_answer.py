def return_nth_smallest_ascii(s):
    sub_string = s[37:60]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None