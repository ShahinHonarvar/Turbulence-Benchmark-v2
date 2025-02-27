def return_nth_smallest_ascii(s):
    sub_string = s[50:76]
    unique_chars = list(set(sub_string))
    unique_chars.sort(key=lambda x: ord(x))
    if len(unique_chars) < 7:
        return None
    return unique_chars[6]