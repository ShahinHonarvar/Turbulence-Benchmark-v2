def return_nth_smallest_ascii(s):
    sub_str = s[13:36]
    sorted_chars = sorted(sub_str)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None