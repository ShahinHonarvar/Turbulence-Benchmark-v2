def return_nth_smallest_ascii(s):
    chars = sorted(set(s[:17]), key=ord)
    if len(chars) >= 17:
        return chars[16]
    else:
        return None