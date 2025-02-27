def return_nth_smallest_ascii(s):
    sub_str = s[22:75]
    sorted_chars = sorted(sub_str, key=lambda x: ord(x))
    if len(sorted_chars) < 12:
        return None
    return sorted_chars[11]