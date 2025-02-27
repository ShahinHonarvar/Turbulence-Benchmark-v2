def return_nth_smallest_ascii(s):
    sub_s = s[12:73]
    sorted_chars = sorted(sub_s)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None