def return_nth_smallest_ascii(s):
    if len(s) < 68:
        return None
    sub_string = s[28:68]
    sorted_chars = sorted(sub_string, key=lambda char: ord(char))
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]