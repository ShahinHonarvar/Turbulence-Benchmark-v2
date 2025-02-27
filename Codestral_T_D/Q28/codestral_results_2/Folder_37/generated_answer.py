def return_nth_smallest_ascii(s):
    substring = s[28:68]
    sorted_chars = sorted(substring)
    return sorted_chars[14] if len(sorted_chars) > 14 else None