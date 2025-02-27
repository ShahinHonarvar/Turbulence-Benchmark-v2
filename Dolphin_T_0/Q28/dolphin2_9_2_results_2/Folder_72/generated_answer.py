def return_nth_smallest_ascii(s):
    sub = s[33:61]
    sorted_chars = sorted(sub, key=lambda c: ord(c))
    return sorted_chars[17]