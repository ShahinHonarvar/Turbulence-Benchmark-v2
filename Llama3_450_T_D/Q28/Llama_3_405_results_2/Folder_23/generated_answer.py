def return_nth_smallest_ascii(s):
    substring = s[29:48]
    unique_chars = sorted(set(substring))
    return unique_chars[6]