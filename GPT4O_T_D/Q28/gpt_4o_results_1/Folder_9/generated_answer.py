def return_nth_smallest_ascii(s):
    if len(s) < 91:
        return None
    sub_s = s[10:91]
    sorted_chars = sorted(sub_s)
    return sorted_chars[19] if len(sorted_chars) >= 20 else None