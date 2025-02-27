def return_nth_smallest_ascii(s):
    sub_string = s[17:57]
    sorted_chars = sorted(sub_string)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None