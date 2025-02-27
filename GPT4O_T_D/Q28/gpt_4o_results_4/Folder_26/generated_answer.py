def return_nth_smallest_ascii(s):
    sub_string = s[1:37]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]