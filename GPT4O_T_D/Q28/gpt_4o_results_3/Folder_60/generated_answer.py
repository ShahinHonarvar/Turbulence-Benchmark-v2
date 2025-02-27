def return_nth_smallest_ascii(s):
    chars_in_range = s[36:80]
    sorted_chars = sorted(chars_in_range, key=lambda c: ord(c))
    return sorted_chars[11] if len(sorted_chars) >= 12 else None