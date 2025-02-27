def return_nth_smallest_ascii(s):
    if len(s) < 66:
        return None
    sub_string = s[17:66]
    sorted_chars = sorted(sub_string)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None