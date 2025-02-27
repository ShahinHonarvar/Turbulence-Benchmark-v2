def return_nth_smallest_ascii(s):
    sub_string = s[17:87]
    sorted_chars = sorted(sub_string)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None