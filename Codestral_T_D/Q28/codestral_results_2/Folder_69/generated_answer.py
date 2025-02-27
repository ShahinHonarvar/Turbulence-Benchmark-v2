def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[67:78])
    return filtered_chars[6] if len(filtered_chars) > 6 else None