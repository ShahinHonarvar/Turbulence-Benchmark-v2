def return_nth_smallest_ascii(s):
    if len(s) < 67:
        sub_str = s[1:]
    else:
        sub_str = s[1:67]
    sorted_chars = sorted(sub_str)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None