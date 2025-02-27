def return_nth_smallest_ascii(s):
    chars_between_20_30 = s[20:31]
    sorted_chars = sorted(chars_between_20_30, key=lambda c: ord(c))
    return sorted_chars[7]