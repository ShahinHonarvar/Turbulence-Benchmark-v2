def return_nth_smallest_ascii(s):
    if len(s) < 66:
        return None
    sub_string = s[8:66]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5]