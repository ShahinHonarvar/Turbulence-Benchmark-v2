def return_nth_smallest_ascii(s):
    if len(s) < 86:
        return ''
    sub = s[33:86]
    sorted_chars = sorted(sub)
    return sorted_chars[12] if len(sorted_chars) >= 13 else ''