def return_nth_smallest_ascii(s):
    sub_string = s[33:61]
    sorted_chars = sorted(sub_string)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None