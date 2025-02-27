def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[10:91])
    return filtered_chars[19] if len(filtered_chars) >= 20 else None