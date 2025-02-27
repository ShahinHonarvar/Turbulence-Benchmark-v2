def return_nth_smallest_ascii(s):
    sub_string = s[29:48]
    sorted_chars = sorted(sub_string)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None