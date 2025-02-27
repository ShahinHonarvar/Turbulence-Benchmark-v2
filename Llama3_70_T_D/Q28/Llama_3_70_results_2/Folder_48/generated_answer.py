def return_nth_smallest_ascii(s):
    sub_string = s[37:60]
    unique_chars = sorted(set(sub_string))
    return unique_chars[5]