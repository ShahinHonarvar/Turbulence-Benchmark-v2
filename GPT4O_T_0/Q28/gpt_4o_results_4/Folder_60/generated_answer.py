def return_nth_smallest_ascii(s):
    sub_string = s[36:80]
    sorted_chars = sorted(sub_string)
    return sorted_chars[11] if len(sorted_chars) >= 12 else None