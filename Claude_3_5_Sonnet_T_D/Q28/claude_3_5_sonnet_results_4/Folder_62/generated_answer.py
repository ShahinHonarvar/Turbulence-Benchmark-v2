def return_nth_smallest_ascii(s):
    substring = s[51:79]
    sorted_chars = sorted(substring)
    if len(sorted_chars) >= 9:
        return sorted_chars[8]
    return None