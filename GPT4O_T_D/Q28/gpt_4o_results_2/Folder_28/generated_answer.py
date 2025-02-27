def return_nth_smallest_ascii(s):
    if len(s) < 78:
        return None
    substring = s[25:78]
    sorted_chars = sorted(substring)
    return sorted_chars[15] if len(sorted_chars) >= 16 else None