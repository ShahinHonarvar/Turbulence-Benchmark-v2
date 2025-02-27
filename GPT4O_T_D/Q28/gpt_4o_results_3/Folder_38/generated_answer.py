def return_nth_smallest_ascii(s):
    if len(s) < 46:
        sub_str = s
    else:
        sub_str = s[:46]
    sorted_chars = sorted(sub_str)
    return sorted_chars[9] if len(sorted_chars) > 9 else None