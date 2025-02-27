def return_nth_smallest_ascii(s):
    target_chars = s[1:32]
    if len(target_chars) < 6:
        return None
    sorted_chars = sorted(target_chars, key=ord)
    return sorted_chars[5]