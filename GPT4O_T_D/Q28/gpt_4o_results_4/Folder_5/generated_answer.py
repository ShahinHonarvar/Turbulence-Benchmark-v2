def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[5:90])
    return filtered_chars[12] if len(filtered_chars) >= 13 else None