def return_nth_smallest_ascii(s):
    substring = s[40:61]
    return sorted(substring, key=lambda c: ord(c))[18]