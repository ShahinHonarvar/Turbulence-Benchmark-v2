def return_nth_smallest_ascii(s):
    substring = s[40:61]
    ascii_chars = sorted(substring, key=ord)
    return ascii_chars[18]