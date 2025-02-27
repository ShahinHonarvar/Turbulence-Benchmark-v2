def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[34:86])
    if len(filtered_chars) < 20:
        return None
    return filtered_chars[19]