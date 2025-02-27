def return_nth_smallest_ascii(s):
    if len(s) < 79:
        return None
    substring = s[51:79]
    sorted_chars = sorted(substring)
    return sorted_chars[8]