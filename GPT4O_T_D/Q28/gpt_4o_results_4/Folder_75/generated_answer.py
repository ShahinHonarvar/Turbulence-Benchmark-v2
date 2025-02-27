def return_nth_smallest_ascii(s):
    sub_string = s[62:84]
    if len(sub_string) < 9:
        return None
    sorted_chars = sorted(sub_string)
    return sorted_chars[8]