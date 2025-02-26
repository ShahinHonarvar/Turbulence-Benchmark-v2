def return_nth_smallest_ascii(s):
    substring = s[14:55]
    sorted_chars = sorted(substring)
    return sorted_chars[10] if len(sorted_chars) > 10 else None