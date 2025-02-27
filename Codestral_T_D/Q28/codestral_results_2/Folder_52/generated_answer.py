def return_nth_smallest_ascii(s):
    sub_s = s[46:73]
    sorted_chars = sorted(sub_s)
    return sorted_chars[14] if len(sorted_chars) > 14 else None