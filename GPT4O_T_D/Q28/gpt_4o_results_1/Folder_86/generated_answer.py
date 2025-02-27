def return_nth_smallest_ascii(s):
    slice_string = s[44:70]
    sorted_chars = sorted(slice_string, key=lambda c: ord(c))
    return sorted_chars[14] if len(sorted_chars) >= 15 else None