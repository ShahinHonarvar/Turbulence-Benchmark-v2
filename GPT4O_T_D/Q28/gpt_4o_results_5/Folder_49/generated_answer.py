def return_nth_smallest_ascii(s):
    if len(s) < 81:
        return None
    substring = s[20:81]
    sorted_chars = sorted(substring)
    return sorted_chars[10] if len(sorted_chars) >= 11 else None