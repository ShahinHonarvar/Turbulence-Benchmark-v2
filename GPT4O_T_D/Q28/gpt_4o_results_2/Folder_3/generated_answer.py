def return_nth_smallest_ascii(s):
    if len(s) < 46:
        return None
    substring = s[25:46]
    sorted_chars = sorted(substring)
    return sorted_chars[10] if len(sorted_chars) > 10 else None