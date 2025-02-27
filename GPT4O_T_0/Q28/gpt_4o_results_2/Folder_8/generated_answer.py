def return_nth_smallest_ascii(s):
    if len(s) < 89:
        return None
    sub_string = s[60:89]
    sorted_chars = sorted(sub_string)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None