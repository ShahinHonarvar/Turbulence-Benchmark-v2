def return_nth_smallest_ascii(s):
    sub = s[60:84]
    sorted_chars = sorted(sub)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None