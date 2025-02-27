def return_nth_smallest_ascii(s):
    if len(s) < 61:
        return None
    substring = s[40:61]
    sorted_chars = sorted(substring)
    return sorted_chars[18] if len(sorted_chars) >= 19 else None