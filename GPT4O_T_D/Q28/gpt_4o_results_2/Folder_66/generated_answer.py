def return_nth_smallest_ascii(s):
    sub_chars = s[35:53]
    if len(sub_chars) < 10:
        return None
    sorted_chars = sorted(sub_chars)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None