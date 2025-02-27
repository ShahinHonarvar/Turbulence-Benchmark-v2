def return_nth_smallest_ascii(s):
    if len(s) < 84:
        return None
    sub_string = s[17:84]
    sorted_chars = sorted(sub_string)
    return sorted_chars[4]