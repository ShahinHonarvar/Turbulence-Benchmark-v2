def return_nth_smallest_ascii(s):
    limited_chars = s[:10]
    sorted_chars = sorted(limited_chars, key=lambda c: ord(c))
    return sorted_chars[9] if len(sorted_chars) >= 10 else None