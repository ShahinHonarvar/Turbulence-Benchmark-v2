def return_nth_smallest_ascii(s):
    if len(s) < 77:
        return None
    segment = s[63:77]
    sorted_chars = sorted(segment)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None