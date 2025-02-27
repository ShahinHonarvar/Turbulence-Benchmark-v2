def return_nth_smallest_ascii(s):
    if len(s) <= 77:
        return None
    substring = s[67:78]
    sorted_chars = sorted(substring)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None