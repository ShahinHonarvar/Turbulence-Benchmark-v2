def return_nth_smallest_ascii(s):
    if len(s) < 83:
        return None
    sub_string = s[10:83]
    sorted_chars = sorted(sub_string)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None