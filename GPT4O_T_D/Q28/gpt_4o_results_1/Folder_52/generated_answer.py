def return_nth_smallest_ascii(s):
    s = s[46:73]
    sorted_chars = sorted(s)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None