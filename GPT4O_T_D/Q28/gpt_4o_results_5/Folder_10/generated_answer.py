def return_nth_smallest_ascii(s):
    sub_chars = s[38:83]
    sorted_chars = sorted(sub_chars)
    return sorted_chars[19] if len(sorted_chars) >= 20 else None