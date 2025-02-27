def return_nth_smallest_ascii(s):
    sub_string = s[40:61]
    sorted_chars = sorted(sub_string, key=lambda x: ord(x))
    if len(sorted_chars) < 19:
        return None
    return sorted_chars[18]