def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[14:55])
    if len(sorted_chars) >= 11:
        return chr(sorted_chars[10])
    else:
        return None