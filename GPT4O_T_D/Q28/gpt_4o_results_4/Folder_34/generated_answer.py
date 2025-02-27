def return_nth_smallest_ascii(s):
    if len(s) < 19:
        return None
    substring = s[:19]
    sorted_chars = sorted(substring)
    return sorted_chars[18] if len(sorted_chars) > 18 else None