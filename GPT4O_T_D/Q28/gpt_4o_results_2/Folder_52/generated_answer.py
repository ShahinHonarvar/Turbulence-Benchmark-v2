def return_nth_smallest_ascii(s):
    sub_chars = s[46:73]
    sorted_chars = sorted(sub_chars)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None