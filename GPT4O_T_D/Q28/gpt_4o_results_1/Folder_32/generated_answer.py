def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    substring = s[14:67]
    sorted_chars = sorted(substring)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None