def return_nth_smallest_ascii(s):
    sub_str = s[33:61]
    if len(sub_str) < 18:
        return None
    sorted_chars = sorted(sub_str)
    return sorted_chars[17]