def return_nth_smallest_ascii(s):
    if len(s) < 53:
        return None
    sub_string = s[3:53]
    sorted_chars = sorted(sub_string)
    return sorted_chars[7]