def return_nth_smallest_ascii(s):
    sub_str = s[62:84]
    sorted_chars = sorted(sub_str)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None