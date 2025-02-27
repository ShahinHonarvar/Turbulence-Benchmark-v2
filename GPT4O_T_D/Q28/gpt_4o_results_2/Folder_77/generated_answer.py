def return_nth_smallest_ascii(s):
    if len(s) < 77:
        return None
    sub_string = s[63:77]
    sorted_chars = sorted(sub_string)
    return sorted_chars[13]