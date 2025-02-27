def return_nth_smallest_ascii(s):
    if len(s) <= 59:
        return None
    substring = s[37:60]
    unique_chars = list(set(substring))
    unique_chars.sort(key=ord)
    if len(unique_chars) < 6:
        return None
    return unique_chars[5]