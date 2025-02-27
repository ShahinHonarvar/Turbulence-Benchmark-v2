def return_nth_smallest_ascii(s):
    if len(s) < 71:
        return None
    sub_str = s[30:71]
    sorted_chars = sorted(sub_str, key=ord)
    return sorted_chars[14] if len(sorted_chars) >= 15 else None