def return_nth_smallest_ascii(s):
    chars = s[15:21]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[5]