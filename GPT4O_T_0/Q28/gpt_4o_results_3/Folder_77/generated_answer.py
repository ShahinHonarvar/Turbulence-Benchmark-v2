def return_nth_smallest_ascii(s):
    sub_string = s[63:77]
    sorted_chars = sorted(sub_string)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None