def return_nth_smallest_ascii(s):
    substring = s[12:73]
    sorted_chars = sorted(substring)
    return sorted_chars[12] if len(sorted_chars) > 12 else None