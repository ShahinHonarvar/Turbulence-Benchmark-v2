def return_nth_smallest_ascii(s):
    sub_string = s[48:77]
    sorted_chars = sorted(sub_string)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None