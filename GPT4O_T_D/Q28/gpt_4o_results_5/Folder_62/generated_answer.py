def return_nth_smallest_ascii(s):
    sub_str = s[51:79]
    sorted_chars = sorted(sub_str, key=lambda x: ord(x))
    if len(sorted_chars) < 9:
        return None
    return sorted_chars[8]