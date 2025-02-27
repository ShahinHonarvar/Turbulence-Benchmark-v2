def return_nth_smallest_ascii(s):
    sub_s = s[60:89]
    sorted_chars = sorted(sub_s)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None