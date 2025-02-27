def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[20:81])
    return sorted_chars[10] if len(sorted_chars) > 10 else None