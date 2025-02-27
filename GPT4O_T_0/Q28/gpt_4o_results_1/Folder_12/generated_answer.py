def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    sub_string = s[3:27]
    sorted_chars = sorted(sub_string)
    return sorted_chars[4]