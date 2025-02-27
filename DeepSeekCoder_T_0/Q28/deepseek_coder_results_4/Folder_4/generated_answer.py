def return_nth_smallest_ascii(s):
    sub_str = s[9:23]
    sorted_chars = sorted(sub_str)
    return sorted_chars[3] if len(sorted_chars) > 3 else None