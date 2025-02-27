def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[62:84])
    return sorted_chars[8] if len(sorted_chars) > 8 else None