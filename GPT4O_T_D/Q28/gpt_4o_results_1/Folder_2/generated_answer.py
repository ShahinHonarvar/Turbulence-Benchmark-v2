def return_nth_smallest_ascii(s):
    sub_string = s[48:77]
    if len(sub_string) < 5:
        return None
    sorted_chars = sorted(sub_string, key=lambda x: ord(x))
    return sorted_chars[4] if len(sorted_chars) >= 5 else None