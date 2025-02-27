def return_nth_smallest_ascii(s):
    if len(s) < 80:
        return None
    sub_str = s[52:80]
    if len(sub_str) < 7:
        return None
    sorted_chars = sorted(sub_str)
    return sorted_chars[6]