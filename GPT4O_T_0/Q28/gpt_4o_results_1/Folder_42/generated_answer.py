def return_nth_smallest_ascii(s):
    if len(s) < 73:
        return None
    sub_string = s[12:73]
    sorted_chars = sorted(sub_string)
    return sorted_chars[12]