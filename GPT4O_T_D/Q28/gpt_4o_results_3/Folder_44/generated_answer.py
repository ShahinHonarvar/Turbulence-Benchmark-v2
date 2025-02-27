def return_nth_smallest_ascii(s):
    substring = s[20:31]
    sorted_chars = sorted(substring)
    return sorted_chars[7] if len(sorted_chars) > 7 else None