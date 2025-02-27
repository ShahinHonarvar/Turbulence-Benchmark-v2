def return_nth_smallest_ascii(s):
    substring = s[38:65]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None