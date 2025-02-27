def return_nth_smallest_ascii(s):
    sub_string = s[4:34]
    if len(sub_string) < 4:
        return None
    sorted_chars = sorted(sub_string)
    return sorted_chars[3]