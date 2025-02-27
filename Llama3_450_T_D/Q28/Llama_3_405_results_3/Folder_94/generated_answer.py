def return_nth_smallest_ascii(s):
    substring = s[6:59]
    unique_chars = sorted(set(substring))
    return unique_chars[18]