def return_nth_smallest_ascii(s):
    target_chars = s[5:48]
    sorted_chars = sorted(target_chars)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None