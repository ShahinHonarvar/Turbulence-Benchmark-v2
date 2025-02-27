def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[33:61], key=ord)
    return sorted_chars[17] if len(sorted_chars) > 17 else None