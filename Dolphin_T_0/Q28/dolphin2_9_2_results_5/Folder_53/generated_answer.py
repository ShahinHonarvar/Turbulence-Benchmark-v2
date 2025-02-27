def return_nth_smallest_ascii(s):
    substring = s[40:61]
    sorted_chars = sorted(list(substring), key=lambda c: ord(c))
    return sorted_chars[-19]