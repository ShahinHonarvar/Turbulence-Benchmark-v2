def return_nth_smallest_ascii(s):
    if len(s) < 67:
        return None
    sub_string = s[1:67]
    sorted_chars = sorted(sub_string)
    return sorted_chars[7]