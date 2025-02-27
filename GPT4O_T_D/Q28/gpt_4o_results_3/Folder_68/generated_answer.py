def return_nth_smallest_ascii(s):
    if len(s) < 11:
        return None
    sorted_chars = sorted(s[:11])
    return sorted_chars[10] if len(sorted_chars) >= 11 else None