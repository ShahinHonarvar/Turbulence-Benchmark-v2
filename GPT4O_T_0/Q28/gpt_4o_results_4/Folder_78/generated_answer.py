def return_nth_smallest_ascii(s):
    if len(s) < 88:
        s = s[:len(s)]
    else:
        s = s[:88]
    sorted_chars = sorted(s)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None