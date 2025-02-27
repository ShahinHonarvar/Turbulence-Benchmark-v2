def return_nth_smallest_ascii(s):
    if len(s) < 23:
        return None
    sliced_section = s[9:23]
    sorted_chars = sorted(sliced_section)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None