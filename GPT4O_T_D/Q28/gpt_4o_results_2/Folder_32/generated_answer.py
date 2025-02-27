def return_nth_smallest_ascii(s):
    sub_s = s[14:67]
    sorted_chars = sorted(sub_s)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None