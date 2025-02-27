def return_nth_smallest_ascii(s):
    if not 0 <= 29 <= 47 < len(s):
        return None
    chars = s[29:48]
    sorted_chars = sorted(chars)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None