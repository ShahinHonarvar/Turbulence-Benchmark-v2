def return_nth_smallest_ascii(s):
    substring = s[17:35]
    sorted_chars = sorted(substring)
    return sorted_chars[17] if len(sorted_chars) > 17 else None