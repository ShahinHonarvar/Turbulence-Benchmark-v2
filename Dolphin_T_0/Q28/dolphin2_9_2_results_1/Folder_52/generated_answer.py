def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[46:73], key=ord)
    if len(sorted_chars) < 15:
        return None
    else:
        return sorted_chars[14]