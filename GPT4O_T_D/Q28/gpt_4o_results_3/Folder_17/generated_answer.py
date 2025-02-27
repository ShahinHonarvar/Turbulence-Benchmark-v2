def return_nth_smallest_ascii(s):
    if len(s) < 34:
        s = s[4:]
    else:
        s = s[4:34]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None