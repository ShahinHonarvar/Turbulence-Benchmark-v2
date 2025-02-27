def return_nth_smallest_ascii(s):
    if len(s) < 68:
        return None
    subset = s[28:68]
    sorted_chars = sorted(subset)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None