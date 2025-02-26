def return_nth_smallest_ascii(s):
    substring = s[9:23]
    sorted_chars = sorted(substring)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None